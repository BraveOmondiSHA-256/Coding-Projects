
from datetime import datetime, timezone

import pandas as pd

from .exchange_client import ExchangeClient
from .indicators import add_indicators
from .strategy import detect_ema_cross
from .trade_manager import TradeManager


def ohlcv_to_dataframe(ohlcv):
    """
    Convert ccxt OHLCV list -> pandas DataFrame

    Columns: timestamp, open, high, low, close, volume, datetime
    """
    df = pd.DataFrame(
        ohlcv,
        columns=["timestamp", "open", "high", "low", "close", "volume"],
    )

    df["datetime"] = df["timestamp"].apply(
        lambda ms: datetime.fromtimestamp(ms / 1000.0, tz=timezone.utc)
    )
    return df


def main():
    symbol = "BTC/USDT"
    timeframe = "1h"

    print("Initialising exchange client...")
    client = ExchangeClient()

    # Live trade manager with low-leverage plan parameters
    tm = TradeManager(
        account_size=1000.0,
        risk_per_trade=0.01,
        atr_mult_entry=1.5,
        rr_tp1=1.0,
        rr_tp2=2.0,
        rr_tp3=3.0,
        tp1_frac=0.3,
        tp2_frac=0.3,
        tp3_frac=0.4,
        atr_mult_trail=1.5,
        fee_rate=0.0004,
    )

    print("Checking server time (ms):", client.get_server_time())

    print(f"Fetching {symbol} {timeframe} candles...")
    raw_ohlcv = client.fetch_ohlcv(symbol, timeframe=timeframe, limit=200)

    df = ohlcv_to_dataframe(raw_ohlcv)
    df = add_indicators(df, ema_fast=9, ema_slow=21, atr_period=14)

    print("\nLast 5 candles with indicators:")
    print(
        df.tail()[[
            "datetime",
            "open",
            "high",
            "low",
            "close",
            "volume",
            "ema_9",
            "ema_21",
            "atr_14",
        ]]
    )

    # --- Strategy logic on the last closed candle ---
    signal = detect_ema_cross(df)
    last_row = df.iloc[-1]

    last_price = float(last_row["close"])
    last_high = float(last_row["high"])
    last_low = float(last_row["low"])
    last_atr = float(last_row["atr_14"])

    print("\nSignal on last candle:", signal)

    # 1) Manage existing position on this candle (SL/TPs/trailing)
    if tm.has_open_position():
        result = tm.manage_open_position(
            high=last_high,
            low=last_low,
            close=last_price,
            atr_value=last_atr,
        )
        if result:
            print(f"Position updated/closed via {result} on this candle.")
        else:
            print("Position still open; no SL/TP hit on this candle.")
    else:
        print("No open position currently.")

    # 2) If flat and signal present, open a new trade using full plan logic
    if not tm.has_open_position() and signal in ("LONG", "SHORT"):
        pos = tm.open_position(
            side=signal,
            entry_price=last_price,
            atr_value=last_atr,
        )
        if pos:
            print("\nOpened new paper trade:")
            print(pos)
        else:
            print("\nSignal present but could not open position (maybe ATR=0?).")

    # Ignore real balance for now (no API keys)
    try:
        usdt_balance = client.get_balance("USDT")
        print(f"\n💰 USDT balance (exchange): {usdt_balance}")
    except Exception as e:
        print("\nCould not fetch balance (probably no API keys or permissions yet):")
        print(e)


if __name__ == "__main__":
    main()