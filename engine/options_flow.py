import pandas as pd
import numpy as np

def generate_options_flow(symbol):

    data = []

    strikes = [350,360,370,380,390,400]

    for strike in strikes:

        size = np.random.randint(100,2000)

        premium = size * np.random.uniform(1,5) * 100

        side = np.random.choice(["BUY","SELL"])

        option_type = np.random.choice(["CALL","PUT"])

        if option_type=="CALL" and side=="BUY":
            signal="Bullish"

        elif option_type=="PUT" and side=="BUY":
            signal="Bearish"

        else:
            signal="Neutral"

        score = np.random.uniform(5,10)

        data.append({
            "symbol":symbol,
            "strike":strike,
            "type":option_type,
            "side":side,
            "size":size,
            "premium":round(premium,2),
            "signal":signal,
            "score":round(score,2)
        })

    return pd.DataFrame(data)
