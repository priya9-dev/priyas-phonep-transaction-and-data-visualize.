import streamlit as st
import pandas as pd
import plotly.express as px

trend_df = pd.read_csv("trend.csv")
st.title("Transaction Trends")

option = st.selectbox("Compare Trend By", ["month", "quarter"])
fig = px.line(trend_df, x=option, y="amount", color="category", title="Trend of Transaction Amount")
st.plotly_chart(fig)

fig2 = px.bar(trend_df, x=option, y="transaction_count", color="category", barmode="group", title="Trend of Transaction Count")
st.plotly_chart(fig2)
