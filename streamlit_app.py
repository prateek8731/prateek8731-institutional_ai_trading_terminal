import streamlit as st

from engine.data_loader import load_data
from engine.market_structure import detect_structure
from engine.liquidity_engine import detect_liquidity
from engine.fvg_engine import detect_fvg
from engine.orderblock_engine import detect_orderblocks
from engine.sweep_engine import detect_sweeps
from engine.ai_predictor import predict_direction
from engine.options_flow import generate_options_flow

from visualization.charts import plot_chart
from visualization.flow_dashboard import show_flow

st.set_page_config(layout="wide")

st.title("Institutional AI Trading Terminal")

symbol = st.sidebar.text_input("Symbol","TSLA")

data = load_data(symbol)

structure = detect_structure(data)
liquidity = detect_liquidity(data)
fvg = detect_fvg(data)
orderblocks = detect_orderblocks(data)
sweeps = detect_sweeps(data)

direction = predict_direction(data)

flow = generate_options_flow(symbol)

col1,col2,col3,col4 = st.columns(4)

col1.metric("AI Direction",direction)
col2.metric("Liquidity Zones",len(liquidity))
col3.metric("FVG Zones",len(fvg))
col4.metric("Sweeps",len(sweeps))

fig = plot_chart(data)

st.plotly_chart(fig,use_container_width=True)

show_flow(flow)

st.subheader("Market Structure")
st.write(structure)
