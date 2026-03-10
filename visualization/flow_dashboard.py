import streamlit as st

def show_flow(df):

    st.subheader("Live Options Flow")

    st.dataframe(df)

    bullish=df[df.signal=="Bullish"]
    bearish=df[df.signal=="Bearish"]

    col1,col2=st.columns(2)

    col1.metric("Bullish Flow",len(bullish))
    col2.metric("Bearish Flow",len(bearish))
