from datetime import datetime, timezone
from pathlib import Path
from typing import List, Dict, Any, Optional

import pandas as pd

from .exchange_client import ExchangeClient
from .indicators import add_indicators




def ohlcv_to_dataframe(ohlcv: List[List[float]]) -> pd.DataFrame:
    """
    Convert ccxt-style OHLCV list -> pandas DataFrame.

    Each row of `ohlcv` looks like:
        [ timestamp_ms, open, high, low, close, volume ]
    """
    df = pd.DataFrame(
        ohlcv,
        columns=["timestamp", "open", "high", "low", "close", "volume"],
    )

    # Convert ms -> proper UTC datetime and use as index
    df["datetime"] = df["timestamp"].apply(
        lambda ms: datetime.fromtimestamp(ms / 1000.0, tz=timezone.utc)
    )
    df.set_index("datetime", inplace=True)

    return df


def generate_signal(prev_row, row) -> Optional[str]:
    """
    EMA crossover logic for a SINGLE step (candle-close confirmed).

    - LONG  when ema_9 crosses ABOVE ema_21
    - SHORT when ema_9 crosses BELOW ema_21
    - None  otherwise
    """
    prev_fast = prev_row["ema_9"]
    prev_slow = prev_row["ema_21"]
    curr_fast = row["ema_9"]
    curr_slow = row["ema_21"]

    # Bullish cross: fast goes from below to above
    if prev_fast <= prev_slow and curr_fast > curr_slow:
        return "LONG"

    # Bearish cross: fast goes from above to below
    if prev_fast >= prev_slow and curr_fast < curr_slow:
        return "SHORT"

    return None


def run_backtest(
    symbol: str = "BTC/USDT",
    timeframe: str = "1h",
    limit: int = 1000,
    initial_equity: float = 1000.0,
    risk_per_trade: float = 0.01,    # 1% risk per trade
    atr_mult_entry: float = 1.5,     # stop distance = atr_mult_entry * ATR
    rr_tp1: float = 1.0,             # TP1 at 1R
    rr_tp2: float = 2.0,             # TP2 at 2R
    rr_tp3: float = 3.0,             # TP3 / runner at 3R (plus trail)
    tp1_frac: float = 0.3,           # 30% size at TP1
    tp2_frac: float = 0.3,           # 30% size at TP2
    tp3_frac: float = 0.4,           # 40% left to run
    fee_rate: float = 0.0004,        # 0.04% per side
    atr_mult_trail: float = 1.5,     # trailing stop: price ± atr_mult_trail * ATR
) -> Dict[str, Any]:
    """
    Backtest aligned with the low-leverage plan:

    - EMA(9/21) crossover with candle-close confirmation
    - ATR-based stop distance and position sizing
    - Fixed % risk per trade
    - Partial TPs: TP1, TP2, TP3
    - After TP1: move SL to break-even
    - After TP2: enable trailing stop on the remaining position

    NOTE: This is candle-based. If SL and TP can both be touched inside the
    same candle (high/low), we use a *conservative* assumption:
        - SL is checked and processed first.
    """

    client = ExchangeClient()
    print(f"[BACKTEST] Fetching OHLCV for {symbol} {timeframe} (limit={limit})...")
    ohlcv = client.fetch_ohlcv(symbol=symbol, timeframe=timeframe, limit=limit)

    # Convert to DataFrame and add indicators
    df = ohlcv_to_dataframe(ohlcv)
    df = add_indicators(df, ema_fast=9, ema_slow=21, atr_period=14)

    # Drop early rows where indicators are NaN
    df = df.dropna().copy()

    equity = initial_equity
    equity_curve: List[Dict[str, float]] = []
    trades: List[Dict[str, Any]] = []

    # current open position (if any)
    position: Optional[Dict[str, Any]] = None

    for i in range(1, len(df)):
        row = df.iloc[i]
        prev_row = df.iloc[i - 1]
        high = float(row["high"])
        low = float(row["low"])
        close = float(row["close"])
        atr_value = float(row["atr_14"])

        # 1) Manage existing position: SL, partial TPs, trailing
        if position is not None:
            side = position["side"]
            entry_price = position["entry_price"]
            size_total = position["size_total"]
            size_open = position["size_open"]
            sl = position["sl"]

            # --- a) Check stop-loss first (conservative candle assumption) ---
            if side == "LONG" and low <= sl:
                # Entire remaining position stopped out
                exit_price = sl
                gross_pnl = (exit_price - entry_price) * size_open
                notional_entry = entry_price * size_open
                notional_exit = exit_price * size_open
                fees = (notional_entry + notional_exit) * fee_rate
                net_pnl = gross_pnl - fees
                equity += net_pnl

                trades.append(
                    {
                        "entry_time": position["entry_time"],
                        "exit_time": row.name,
                        "side": side,
                        "entry_price": entry_price,
                        "exit_price": exit_price,
                        "size": size_open,
                        "gross_pnl": gross_pnl,
                        "fees": fees,
                        "net_pnl": net_pnl,
                        "exit_reason": "SL",
                        "equity_after": equity,
                    }
                )
                position = None

            elif side == "SHORT" and high >= sl:
                exit_price = sl
                gross_pnl = (entry_price - exit_price) * size_open
                notional_entry = entry_price * size_open
                notional_exit = exit_price * size_open
                fees = (notional_entry + notional_exit) * fee_rate
                net_pnl = gross_pnl - fees
                equity += net_pnl

                trades.append(
                    {
                        "entry_time": position["entry_time"],
                        "exit_time": row.name,
                        "side": side,
                        "entry_price": entry_price,
                        "exit_price": exit_price,
                        "size": size_open,
                        "gross_pnl": gross_pnl,
                        "fees": fees,
                        "net_pnl": net_pnl,
                        "exit_reason": "SL",
                        "equity_after": equity,
                    }
                )
                position = None

            # --- b) If still in trade, process partial TPs ---
            if position is not None:
                size_open = position["size_open"]
                state = position["state"]

                # Helper to process one partial TP
                def hit_partial_tp(
                    label: str,
                    target_price: float,
                    frac: float,
                ):
                    nonlocal equity, size_open, trades, position
                    if size_open <= 0:
                        return

                    # Did this candle reach the target?
                    if side == "LONG" and high >= target_price:
                        size_to_close = min(size_total * frac, size_open)
                    elif side == "SHORT" and low <= target_price:
                        size_to_close = min(size_total * frac, size_open)
                    else:
                        return

                    if size_to_close <= 0:
                        return

                    if side == "LONG":
                        gross = (target_price - entry_price) * size_to_close
                    else:
                        gross = (entry_price - target_price) * size_to_close

                    notional_entry = entry_price * size_to_close
                    notional_exit = target_price * size_to_close
                    fees = (notional_entry + notional_exit) * fee_rate
                    net = gross - fees
                    equity += net

                    size_open -= size_to_close
                    position["size_open"] = size_open

                    trades.append(
                        {
                            "entry_time": position["entry_time"],
                            "exit_time": row.name,
                            "side": side,
                            "entry_price": entry_price,
                            "exit_price": target_price,
                            "size": size_to_close,
                            "gross_pnl": gross,
                            "fees": fees,
                            "net_pnl": net,
                            "exit_reason": label,
                            "equity_after": equity,
                        }
                    )

                # TP1
                if state == "OPEN":
                    hit_partial_tp("TP1", position["tp1"], tp1_frac)
                    if position is not None and position["size_open"] < size_total:
                        # TP1 hit => move SL to BE
                        position["state"] = "TP1_HIT"
                        position["sl"] = entry_price  # break-even

                # TP2
                if position is not None and position["state"] in ("OPEN", "TP1_HIT"):
                    hit_partial_tp("TP2", position["tp2"], tp2_frac)
                    # If we closed at least TP1+TP2 portions, mark TP2_HIT
                    if position is not None and position["size_open"] <= size_total * tp3_frac:
                        position["state"] = "TP2_HIT"
                        position["trail_active"] = True

                # TP3 (runner)
                if position is not None and position["state"] in ("OPEN", "TP1_HIT", "TP2_HIT"):
                    # Close remaining at TP3 (if hit)
                    hit_partial_tp("TP3", position["tp3"], 1.0)  # up to all remaining
                    if position is not None and position["size_open"] <= 0:
                        position = None  # fully closed on TPs

            # --- c) If still in trade after partials, apply trailing stop (post-TP2) ---
            if position is not None and position.get("trail_active", False):
                # Trailing off the candle close
                if side == "LONG":
                    new_sl = close - atr_mult_trail * atr_value
                    # Never move stop down
                    position["sl"] = max(position["sl"], new_sl)
                else:  # SHORT
                    new_sl = close + atr_mult_trail * atr_value
                    # Never move stop up (for shorts)
                    position["sl"] = min(position["sl"], new_sl)

        # 2) If flat, look for new entry signal
        if position is None:
            signal = generate_signal(prev_row, row)

            if signal in ("LONG", "SHORT") and atr_value > 0:
                # Risk per trade in account currency
                risk_amount = equity * risk_per_trade

                # Stop distance based on ATR
                stop_distance = atr_value * atr_mult_entry
                if stop_distance <= 0:
                    equity_curve.append({"time": row.name, "equity": equity})
                    continue

                # Position size in base asset
                size_total = risk_amount / stop_distance
                if size_total <= 0:
                    equity_curve.append({"time": row.name, "equity": equity})
                    continue

                entry_price = close

                if signal == "LONG":
                    sl = entry_price - stop_distance
                    tp1 = entry_price + stop_distance * rr_tp1
                    tp2 = entry_price + stop_distance * rr_tp2
                    tp3 = entry_price + stop_distance * rr_tp3
                else:  # SHORT
                    sl = entry_price + stop_distance
                    tp1 = entry_price - stop_distance * rr_tp1
                    tp2 = entry_price - stop_distance * rr_tp2
                    tp3 = entry_price - stop_distance * rr_tp3

                if sl <= 0:
                    equity_curve.append({"time": row.name, "equity": equity})
                    continue

                position = {
                    "side": signal,
                    "entry_price": entry_price,
                    "size_total": size_total,
                    "size_open": size_total,
                    "sl": sl,
                    "tp1": tp1,
                    "tp2": tp2,
                    "tp3": tp3,
                    "state": "OPEN",
                    "trail_active": False,
                    "entry_time": row.name,
                    "stop_distance": stop_distance,
                }

        # Track equity at each candle (for equity curve)
        equity_curve.append({"time": row.name, "equity": equity})

    # Convert to DataFrame
    equity_df = pd.DataFrame(equity_curve).set_index("time")

    # ---- Basic performance stats ----
    final_equity = equity
    total_return = (final_equity / initial_equity) - 1.0

    winning_trades = [t for t in trades if t["net_pnl"] > 0]
    losing_trades = [t for t in trades if t["net_pnl"] < 0]

    win_rate = (len(winning_trades) / len(trades)) if trades else 0.0
    avg_win = (
        sum(t["net_pnl"] for t in winning_trades) / len(winning_trades)
        if winning_trades
        else 0.0
    )
    avg_loss = (
        sum(t["net_pnl"] for t in losing_trades) / len(losing_trades)
        if losing_trades
        else 0.0
    )

    # Max drawdown (in %)
    peak = initial_equity
    max_dd = 0.0
    for _, e_row in equity_df.iterrows():
        if e_row["equity"] > peak:
            peak = e_row["equity"]
        dd = (e_row["equity"] / peak) - 1.0
        if dd < max_dd:
            max_dd = dd

    results: Dict[str, Any] = {
        "symbol": symbol,
        "timeframe": timeframe,
        "initial_equity": initial_equity,
        "final_equity": final_equity,
        "total_return_pct": total_return * 100,
        "num_trades": len(trades),
        "win_rate_pct": win_rate * 100,
        "avg_win": avg_win,
        "avg_loss": avg_loss,
        "max_drawdown_pct": max_dd * 100,
        "trades": trades,
        "equity_curve": equity_df,
    }

    return results


def pretty_print_results(results: Dict[str, Any]) -> None:
    print("\n===== BACKTEST RESULTS =====")
    print(f"Symbol          : {results['symbol']}")
    print(f"Timeframe       : {results['timeframe']}")
    print(f"Initial equity  : {results['initial_equity']:.2f}")
    print(f"Final equity    : {results['final_equity']:.2f}")
    print(f"Total return    : {results['total_return_pct']:.2f}%")
    print(f"Number of trades: {results['num_trades']}")
    print(f"Win rate        : {results['win_rate_pct']:.2f}%")
    print(f"Avg win (USDT)  : {results['avg_win']:.4f}")
    print(f"Avg loss (USDT) : {results['avg_loss']:.4f}")
    print(f"Max drawdown    : {results['max_drawdown_pct']:.2f}%")
    print("============================\n")


if __name__ == "__main__":
    print("BACKTEST.PY HAS STARTED (LOW-LEV PLAN VERSION)")

results = run_backtest(
    symbol="BTC/USDT",
    timeframe="1h",
    limit=1000,
    initial_equity=1000.0,
    risk_per_trade=0.01,
    atr_mult_entry=1.5,
    rr_tp1=1.0,
    rr_tp2=2.0,
    rr_tp3=3.0,
    tp1_frac=0.3,
    tp2_frac=0.3,
    tp3_frac=0.4,
    fee_rate=0.0004,
    atr_mult_trail=1.5,
)

pretty_print_results(results)

out_dir = Path("backtests")
out_dir.mkdir(exist_ok=True)

trades_df = pd.DataFrame(results["trades"])
trades_df.to_csv(out_dir / "trades_lowlev.csv", index=False)

equity_df = results["equity_curve"]
equity_df.to_csv(out_dir / "equity_curve_lowlev.csv")

print("Saved CSVs to 'backtests/trades_lowlev.csv' and 'backtests/equity_curve_lowlev.csv'")