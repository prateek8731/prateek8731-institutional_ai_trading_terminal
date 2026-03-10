import yfinance as yf
import pandas as pd


def load_data(symbol="TSLA", interval="5m", period="5d"):

    df = yf.download(
        symbol,
        interval=interval,
        period=period,
        progress=False
    )

    if df.empty:
        raise ValueError("No data returned from yfinance")

    # Reset index
    df.reset_index(inplace=True)

    # Flatten multi-index columns if they exist
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = [col[0] for col in df.columns]

    # Standardize datetime column
    if "Datetime" not in df.columns:
        if "Date" in df.columns:
            df.rename(columns={"Date": "Datetime"}, inplace=True)

    # Keep only required columns
    needed = ["Datetime","Open","High","Low","Close","Volume"]
    df = df[needed]

    # Convert numeric columns safely
    for col in ["Open","High","Low","Close","Volume"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df.dropna(inplace=True)

    return df
