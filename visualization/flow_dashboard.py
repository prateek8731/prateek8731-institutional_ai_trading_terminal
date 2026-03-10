import streamlit as st


def show_flow(df):

    st.subheader("Institutional Options Flow")

    bullish = df[df["Signal"] == "Bullish"]
    bearish = df[df["Signal"] == "Bearish"]

    col1, col2, col3 = st.columns(3)

    col1.metric("Bullish Flow", len(bullish))
    col2.metric("Bearish Flow", len(bearish))
    col3.metric("Total Trades", len(df))

    st.dataframe(df, use_container_width=True)
