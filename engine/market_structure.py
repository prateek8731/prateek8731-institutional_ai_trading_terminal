import pandas as pd


def detect_structure(df):
    """
    Detect Higher Highs and Lower Lows in price structure.
    Returns a list of detected structure points.
    """

    structure = []

    # Ensure numeric
    df = df.copy()
    df["High"] = pd.to_numeric(df["High"])
    df["Low"] = pd.to_numeric(df["Low"])

    for i in range(2, len(df)):

        current_high = float(df["High"].iloc[i])
        prev_high = float(df["High"].iloc[i - 1])
        prev2_high = float(df["High"].iloc[i - 2])

        current_low = float(df["Low"].iloc[i])
        prev_low = float(df["Low"].iloc[i - 1])
        prev2_low = float(df["Low"].iloc[i - 2])

        # Higher High
        if current_high > prev_high and current_high > prev2_high:
            structure.append({
                "type": "Higher High",
                "index": i,
                "price": current_high
            })

        # Lower Low
        if current_low < prev_low and current_low < prev2_low:
            structure.append({
                "type": "Lower Low",
                "index": i,
                "price": current_low
            })

    return structure
