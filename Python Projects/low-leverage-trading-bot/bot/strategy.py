def detect_ema_cross(df):
    """
    Detect if EMA 9 just crossed EMA 21 on the LAST candle.

    Returns:
        "LONG"  -> bullish cross (ema9 crosses ABOVE ema21)
        "SHORT" -> bearish cross (ema9 crosses BELOW ema21)
        None    -> no signal
    """
    if len(df) < 3:
        return None

    # previous candle
    prev_ema9 = df["ema_9"].iloc[-2]
    prev_ema21 = df["ema_21"].iloc[-2]

    # current candle
    curr_ema9 = df["ema_9"].iloc[-1]
    curr_ema21 = df["ema_21"].iloc[-1]

    # Bullish cross → Long
    if prev_ema9 < prev_ema21 and curr_ema9 > curr_ema21:
        return "LONG"

    # Bearish cross → Short
    if prev_ema9 > prev_ema21 and curr_ema9 < curr_ema21:
        return "SHORT"

    return None


def calculate_atr_stop(entry_price, atr_value, multiplier=1.5):
    """
    ATR-based stop loss.

    Example:
    entry_price = 100
    atr = 2
    multiplier = 1.5
    stop_distance = 2 * 1.5 = 3

    Long stop  = 100 - 3
    Short stop = 100 + 3
    """
    stop_distance = atr_value * multiplier
    long_stop = entry_price - stop_distance
    short_stop = entry_price + stop_distance
    return long_stop, short_stop
