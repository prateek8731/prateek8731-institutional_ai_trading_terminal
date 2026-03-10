import yfinance as yf
import pandas as pd


def load_data(symbol="BTC-USD", interval="5m", period="5d"):
    """
    Download market data and normalize column names
    """

    df = yf.download(
        symbol,
        interval=interval,
        period=period,
        progress=False
    )

    if df.empty:
        raise ValueError("No data returned from yfinance.")

    df.reset_index(inplace=True)

    # Ensure datetime column name
    if "Datetime" not in df.columns:
        if "Date" in df.columns:
            df.rename(columns={"Date": "Datetime"}, inplace=True)

    return df
