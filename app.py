import streamlit as st
import pandas as pd
import numpy as np

st.title("AI Traffic Monitoring Dashboard")

st.write("Simple dashboard deployed from Streamlit")

data = pd.DataFrame(
    np.random.randn(20,3),
    columns=["Cars","Bikes","Buses"]
)

st.line_chart(data)

st.success("Dashboard is running successfully 🚀")
