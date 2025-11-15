from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

import json


@dataclass
class Position:
    """
    Represents a single open trade with partial TP logic.

    - size_total: full position size opened at entry
    - size_open: remaining open size (after partials)
    - state: "OPEN" -> "TP1_HIT" -> "TP2_HIT" -> "CLOSED"
    - trail_active: trailing stop on/off (after TP2)
    """
    side: str                  # "LONG" or "SHORT"
    entry_price: float
    size_total: float
    size_open: float
    stop_loss: float
    tp1: float
    tp2: float
    tp3: float
    opened_at: str             # ISO timestamp
    state: str = "OPEN"
    trail_active: bool = False

    exit_price: float | None = None
    closed_at: str | None = None
    pnl: float | None = None
    exit_reason: str | None = None


class TradeManager:
    """
    Live/paper Trade Manager that matches the low-leverage plan logic:

    - Fixed % risk per trade (based on current equity)
    - ATR-based stop distance
    - Partial take profits at TP1, TP2, TP3
    - Move SL to break-even after TP1
    - Enable trailing stop after TP2
    """

    def __init__(
        self,
        account_size: float = 1000.0,
        risk_per_trade: float = 0.01,   # 1% per trade
        atr_mult_entry: float = 1.5,    # stop distance = atr_mult_entry * ATR
        rr_tp1: float = 1.0,            # TP1 at 1R
        rr_tp2: float = 2.0,            # TP2 at 2R
        rr_tp3: float = 3.0,            # TP3 at 3R
        tp1_frac: float = 0.3,          # 30% at TP1
        tp2_frac: float = 0.3,          # 30% at TP2
        tp3_frac: float = 0.4,          # 40% runner
        atr_mult_trail: float = 1.5,    # trailing stop distance
        fee_rate: float = 0.0004,       # 0.04% per side
        log_dir: str = "logs",
    ) -> None:
        # "Equity" is tracked internally and updated with PnL
        self.equity = account_size
        self.risk_per_trade = risk_per_trade
        self.atr_mult_entry = atr_mult_entry
        self.rr_tp1 = rr_tp1
        self.rr_tp2 = rr_tp2
        self.rr_tp3 = rr_tp3
        self.tp1_frac = tp1_frac
        self.tp2_frac = tp2_frac
        self.tp3_frac = tp3_frac
        self.atr_mult_trail = atr_mult_trail
        self.fee_rate = fee_rate

        self.position: Position | None = None

        self.log_dir = Path(log_dir)
        self.log_dir.mkdir(parents=True, exist_ok=True)

    # ---------- Helper methods ----------

    def has_open_position(self) -> bool:
        return self.position is not None and self.position.state != "CLOSED"

    def _now_iso(self) -> str:
        return datetime.now(tz=timezone.utc).isoformat()

    def _log_event(self, event_type: str, payload: dict) -> None:
        """
        Append a JSON line to logs/trades.log so you can inspect later.
        """
        payload_with_meta = {
            "timestamp": self._now_iso(),
            "event_type": event_type,
            "equity": self.equity,
            **payload,
        }
        log_path = self.log_dir / "trades.log"
        with log_path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(payload_with_meta) + "\n")

    # ---------- Core trading actions ----------

    def open_position(
        self,
        side: str,
        entry_price: float,
        atr_value: float,
    ) -> Optional[Position]:
        """
        Open a new position using the low-leverage plan logic.

        Uses:
        - self.equity (current equity)
        - self.risk_per_trade
        - ATR-based stop distance
        - R-multiples for TP1, TP2, TP3
        """
        if self.has_open_position():
            # Already in a trade; skip
            return None

        side = side.upper()
        if side not in ("LONG", "SHORT"):
            raise ValueError(f"Unsupported side: {side}")

        if atr_value <= 0:
            return None

        # 1) Risk amount in account currency
        risk_amount = self.equity * self.risk_per_trade

        # 2) Stop distance based on ATR
        stop_distance = atr_value * self.atr_mult_entry
        if stop_distance <= 0:
            return None

        # 3) Position size in base asset
        size_total = risk_amount / stop_distance
        if size_total <= 0:
            return None

        # 4) Stops and Targets
        if side == "LONG":
            stop_loss = entry_price - stop_distance
            tp1 = entry_price + stop_distance * self.rr_tp1
            tp2 = entry_price + stop_distance * self.rr_tp2
            tp3 = entry_price + stop_distance * self.rr_tp3
        else:  # SHORT
            stop_loss = entry_price + stop_distance
            tp1 = entry_price - stop_distance * self.rr_tp1
            tp2 = entry_price - stop_distance * self.rr_tp2
            tp3 = entry_price - stop_distance * self.rr_tp3

        if stop_loss <= 0:
            return None

        pos = Position(
            side=side,
            entry_price=entry_price,
            size_total=size_total,
            size_open=size_total,
            stop_loss=stop_loss,
            tp1=tp1,
            tp2=tp2,
            tp3=tp3,
            opened_at=self._now_iso(),
        )

        self.position = pos
        self._log_event("OPEN", asdict(pos))

        return pos

    def _close_remaining(self, exit_price: float, reason: str) -> Optional[Position]:
        """
        Close all remaining size at exit_price (SL or final TP).
        """
        if not self.has_open_position():
            return None

        pos = self.position
        assert pos is not None  # type checker

        side = pos.side
        size = pos.size_open

        if size <= 0:
            return None

        if side == "LONG":
            gross_pnl = (exit_price - pos.entry_price) * size
        else:  # SHORT
            gross_pnl = (pos.entry_price - exit_price) * size

        notional_entry = pos.entry_price * size
        notional_exit = exit_price * size
        fees = (notional_entry + notional_exit) * self.fee_rate
        net_pnl = gross_pnl - fees

        self.equity += net_pnl

        pos.size_open = 0.0
        pos.exit_price = exit_price
        pos.closed_at = self._now_iso()
        pos.pnl = net_pnl
        pos.exit_reason = reason
        pos.state = "CLOSED"

        self._log_event("CLOSE", asdict(pos))

        # Clear the in-memory position
        self.position = None

        return pos

    def _partial_tp(self, label: str, target_price: float, frac: float, high: float, low: float) -> None:
        """
        Handle a partial take-profit if price hit target this candle.
        Logs the partial and updates equity + size_open.
        """
        if not self.has_open_position():
            return

        pos = self.position
        assert pos is not None

        side = pos.side
        size_total = pos.size_total
        size_open = pos.size_open

        if size_open <= 0:
            return

        # Check if target was hit this candle
        if side == "LONG":
            if high < target_price:
                return
        else:  # SHORT
            if low > target_price:
                return

        # How much to close
        size_to_close = min(size_total * frac, size_open)
        if size_to_close <= 0:
            return

        if side == "LONG":
            gross_pnl = (target_price - pos.entry_price) * size_to_close
        else:
            gross_pnl = (pos.entry_price - target_price) * size_to_close

        notional_entry = pos.entry_price * size_to_close
        notional_exit = target_price * size_to_close
        fees = (notional_entry + notional_exit) * self.fee_rate
        net_pnl = gross_pnl - fees

        self.equity += net_pnl
        size_open -= size_to_close
        pos.size_open = size_open

        payload = {
            "side": side,
            "entry_price": pos.entry_price,
            "exit_price": target_price,
            "size_closed": size_to_close,
            "gross_pnl": gross_pnl,
            "fees": fees,
            "net_pnl": net_pnl,
            "tp_label": label,
            "state": pos.state,
        }
        self._log_event(label, payload)

    def manage_open_position(
        self,
        high: float,
        low: float,
        close: float,
        atr_value: float,
    ) -> Optional[str]:
        """
        Manage the current position using the last closed candle.

        This matches the backtest logic:

        1) Check SL
        2) TP1 (partial, move SL to BE)
        3) TP2 (partial, enable trail)
        4) TP3 (partial/final)
        5) Trailing stop update (after TP2)
        """
        if not self.has_open_position():
            return None

        pos = self.position
        assert pos is not None
        side = pos.side

        # --- 1) Check stop-loss first (conservative) ---
        sl = pos.stop_loss
        if side == "LONG" and low <= sl:
            self._close_remaining(sl, reason="SL")
            return "SL"

        if side == "SHORT" and high >= sl:
            self._close_remaining(sl, reason="SL")
            return "SL"

        # --- 2) Partial TPs ---
        # TP1
        if pos.state == "OPEN":
            self._partial_tp("TP1", pos.tp1, self.tp1_frac, high, low)
            # If any size was closed, move SL to BE
            if pos.size_open < pos.size_total:
                pos.state = "TP1_HIT"
                pos.stop_loss = pos.entry_price  # break-even

        # TP2
        if self.has_open_position() and pos.state in ("OPEN", "TP1_HIT"):
            self._partial_tp("TP2", pos.tp2, self.tp2_frac, high, low)
            # If only runner left, mark TP2_HIT and activate trailing
            if self.has_open_position() and pos.size_open <= pos.size_total * self.tp3_frac:
                pos.state = "TP2_HIT"
                pos.trail_active = True

        # TP3 (runner)
        if self.has_open_position() and pos.state in ("OPEN", "TP1_HIT", "TP2_HIT"):
            # Close remaining at TP3 if hit
            self._partial_tp("TP3", pos.tp3, 1.0, high, low)
            # If everything was closed due to TP3 partial, position may still be present with size_open=0
            if self.has_open_position() and pos.size_open <= 0:
                self._close_remaining(pos.tp3, reason="TP3_FULL")
                return "TP3_FULL"

        # --- 3) Trailing stop after TP2 ---
        if self.has_open_position() and pos.trail_active and atr_value > 0:
            if side == "LONG":
                new_sl = close - self.atr_mult_trail * atr_value
                pos.stop_loss = max(pos.stop_loss, new_sl)
            else:  # SHORT
                new_sl = close + self.atr_mult_trail * atr_value
                pos.stop_loss = min(pos.stop_loss, new_sl)

            self._log_event(
                "TRAIL_UPDATE",
                {
                    "side": side,
                    "entry_price": pos.entry_price,
                    "new_stop_loss": pos.stop_loss,
                    "close": close,
                    "atr_value": atr_value,
                    "state": pos.state,
                },
            )

        return None