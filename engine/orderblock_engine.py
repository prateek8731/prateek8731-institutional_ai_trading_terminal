def detect_orderblocks(df):
    """
    Detect basic bullish / bearish order blocks
    """

    blocks = []

    for i in range(1, len(df)):

        prev_open = df["Open"].iloc[i-1]
        prev_close = df["Close"].iloc[i-1]

        current_open = df["Open"].iloc[i]
        current_close = df["Close"].iloc[i]

        # Bullish OB
        if prev_close < prev_open and current_close > current_open:
            blocks.append({
                "type": "Bullish Order Block",
                "index": i-1,
                "price": prev_open
            })

        # Bearish OB
        if prev_close > prev_open and current_close < current_open:
            blocks.append({
                "type": "Bearish Order Block",
                "index": i-1,
                "price": prev_open
            })

    return blocks
