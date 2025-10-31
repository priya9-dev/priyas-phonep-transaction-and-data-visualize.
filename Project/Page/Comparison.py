import streamlit as st
import pandas as pd
import plotly.express as px

compare_df = pd.read_csv("comparison.csv")
st.title("Region/Type Comparison")

region = st.selectbox("Select Region", compare_df["region"].unique())
type_choice = st.selectbox("Select Transaction Type", compare_df["type"].unique())

filtered = compare_df[(compare_df["region"] == region) & (compare_df["type"] == type_choice)]

st.subheader(f"Comparison: {region} / {type_choice}")
st.dataframe(filtered)

# Faceted bar plot
fig1 = px.bar(compare_df, x="region", y="amount", color="type", barmode="group", title="Grouped Bar by Region & Type")
st.plotly_chart(fig1)

# Pie chart
fig2 = px.pie(compare_df, names="type", values="amount", title="Transactions by Type")
st.plotly_chart(fig2)
