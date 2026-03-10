import pandas as pd
import numpy as np


def generate_options_flow(symbol):

    strikes = [300,320,340,360,380,400,420]

    rows = []

    for strike in strikes:

        option_type = np.random.choice(["CALL","PUT"])
        side = np.random.choice(["BUY","SELL"])

        size = np.random.randint(100,2000)

        premium = size * np.random.uniform(1.5,6) * 100

        if option_type == "CALL" and side == "BUY":
            signal = "Bullish"

        elif option_type == "PUT" and side == "BUY":
            signal = "Bearish"

        else:
            signal = "Neutral"

        score = round(np.random.uniform(5,10),2)

        rows.append({
            "Symbol": symbol,
            "Strike": strike,
            "Type": option_type,
            "Side": side,
            "Contracts": size,
            "Premium": round(premium,2),
            "Signal": signal,
            "Score": score
        })

    df = pd.DataFrame(rows)

    return df
