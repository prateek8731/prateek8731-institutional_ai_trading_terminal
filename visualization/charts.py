import plotly.graph_objects as go


def plot_chart(df):

    fig = go.Figure()

    fig.add_trace(go.Candlestick(
        x=df["Datetime"],
        open=df["Open"],
        high=df["High"],
        low=df["Low"],
        close=df["Close"],
        name="Price"
    ))

    fig.update_layout(
        title="Market Chart",
        xaxis_title="Time",
        yaxis_title="Price",
        template="plotly_dark",
        height=700
    )

    return fig
