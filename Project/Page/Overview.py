import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("transactions.csv")
summary = df.groupby('category')['amount'].sum().reset_index()

st.title("Overview Page")
st.subheader("Transaction Summary")
st.dataframe(summary)

fig1 = px.pie(summary, names='category', values='amount', title="Transaction Categories Donut Chart")
st.plotly_chart(fig1)

fig2 = px.bar(summary, x='category', y='amount', title="Transaction Bar Plot")
st.plotly_chart(fig2)

# Choropleth map example, assuming 'state' and 'amount'
if 'state' in df:
    fig3 = px.choropleth(df, locations='state', locationmode='USA-states',
                         color='amount', title="Transaction by State")
    st.plotly_chart(fig3)

