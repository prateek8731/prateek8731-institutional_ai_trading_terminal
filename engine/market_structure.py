def detect_structure(df):
    """
    Detect Higher Highs / Lower Lows
    """

    structure = []

    for i in range(2, len(df)):

        prev_high = df["High"].iloc[i-1]
        prev2_high = df["High"].iloc[i-2]

        prev_low = df["Low"].iloc[i-1]
        prev2_low = df["Low"].iloc[i-2]

        current_high = df["High"].iloc[i]
        current_low = df["Low"].iloc[i]

        if current_high > prev_high and current_high > prev2_high:
            structure.append({
                "type": "Higher High",
                "index": i,
                "price": current_high
            })

        if current_low < prev_low and current_low < prev2_low:
            structure.append({
                "type": "Lower Low",
                "index": i,
                "price": current_low
            })

    return structure
