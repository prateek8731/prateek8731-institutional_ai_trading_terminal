import numpy as np
from sklearn.ensemble import RandomForestClassifier


def predict_direction(df):

    df = df.copy()

    df["return"] = df["Close"].pct_change()

    df["target"] = np.where(df["return"] > 0, 1, 0)

    df.dropna(inplace=True)

    features = df[["Open", "High", "Low", "Close", "Volume"]]

    target = df["target"]

    model = RandomForestClassifier(
        n_estimators=200,
        random_state=42
    )

    model.fit(features, target)

    prediction = model.predict(features.tail(1))[0]

    if prediction == 1:
        return "Bullish"

    return "Bearish"
