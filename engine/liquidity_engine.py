import pandas as pd


def detect_liquidity(df, window=15):
    """
    Detect buy side / sell side liquidity zones
    """

    zones = []

    rolling_high = df["High"].rolling(window).max()
    rolling_low = df["Low"].rolling(window).min()

    for i in range(window, len(df)):

        if df["High"].iloc[i] >= rolling_high.iloc[i]:
            zones.append({
                "type": "Buy Side Liquidity",
                "index": i,
                "price": df["High"].iloc[i]
            })

        if df["Low"].iloc[i] <= rolling_low.iloc[i]:
            zones.append({
                "type": "Sell Side Liquidity",
                "index": i,
                "price": df["Low"].iloc[i]
            })

    return zones
