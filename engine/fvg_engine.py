def detect_fvg(df):
    """
    Detect Fair Value Gaps
    """

    gaps = []

    for i in range(2, len(df)):

        high_2 = df["High"].iloc[i-2]
        low_2 = df["Low"].iloc[i-2]

        current_low = df["Low"].iloc[i]
        current_high = df["High"].iloc[i]

        # Bullish imbalance
        if current_low > high_2:
            gaps.append({
                "type": "Bullish FVG",
                "index": i,
                "top": current_low,
                "bottom": high_2
            })

        # Bearish imbalance
        if current_high < low_2:
            gaps.append({
                "type": "Bearish FVG",
                "index": i,
                "top": low_2,
                "bottom": current_high
            })

    return gaps
