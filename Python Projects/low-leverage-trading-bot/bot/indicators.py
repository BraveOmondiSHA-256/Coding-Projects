import pandas as pd


def ema(series: pd.Series, period: int) -> pd.Series:
    """
    Exponential Moving Average (EMA).

    Intuition:
    - Like a normal moving average but gives more weight to recent candles.
    - Period = how many candles it "looks back" over (rough idea).
    """
    return series.ewm(span=period, adjust=False).mean()


def add_ema(df: pd.DataFrame, period: int, col_name: str | None = None) -> pd.DataFrame:
    """
    Add an EMA of the 'close' price to the DataFrame.
    """
    if col_name is None:
        col_name = f"ema_{period}"

    df[col_name] = ema(df["close"], period)
    return df


def add_atr(df: pd.DataFrame, period: int = 14, col_name: str | None = None) -> pd.DataFrame:
    """
    Average True Range (ATR) - measures volatility.

    True Range (TR) for each candle:
    - high - low
    - |high - previous_close|
    - |low - previous_close|
    Take the maximum of those three.

    ATR = smoothed average of TR over 'period' candles.
    """
    if col_name is None:
        col_name = f"atr_{period}"

    high = df["high"]
    low = df["low"]
    close = df["close"]

    prev_close = close.shift(1)

    tr1 = high - low
    tr2 = (high - prev_close).abs()
    tr3 = (low - prev_close).abs()

    true_range = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)

    df[col_name] = true_range.ewm(span=period, adjust=False).mean()
    return df


def add_indicators(
    df: pd.DataFrame,
    ema_fast: int = 9,
    ema_slow: int = 21,
    atr_period: int = 14,
) -> pd.DataFrame:
    """
    Convenience helper to add all indicators we care about.
    """
    df = add_ema(df, ema_fast, col_name=f"ema_{ema_fast}")
    df = add_ema(df, ema_slow, col_name=f"ema_{ema_slow}")
    df = add_atr(df, atr_period, col_name=f"atr_{atr_period}")
    return df
