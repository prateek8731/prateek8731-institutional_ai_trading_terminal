def detect_sweeps(df, lookback=10):
    """
    Detect liquidity sweeps (stop hunts)
    """

    sweeps = []

    for i in range(lookback, len(df)):

        previous_high = df["High"].iloc[i-lookback:i].max()
        previous_low = df["Low"].iloc[i-lookback:i].min()

        current_high = df["High"].iloc[i]
        current_low = df["Low"].iloc[i]

        if current_high > previous_high:
            sweeps.append({
                "type": "High Sweep",
                "index": i,
                "price": current_high
            })

        if current_low < previous_low:
            sweeps.append({
                "type": "Low Sweep",
                "index": i,
                "price": current_low
            })

    return sweeps
