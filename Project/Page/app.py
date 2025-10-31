import streamlit as st
import pandas as pd
import plotly.express as px
import mysql.connector

# MySQL connection
conn = mysql.connector.connect(host='localhost', user='root', password='yourpassword', database='mydb')
df = pd.read_sql('SELECT * FROM transactions', conn)
conn.close()

st.title("Transaction Dashboard")

st.subheader("Full Data")
st.dataframe(df)

# Simple Category Summary
summary = df.groupby('category')['amount'].sum().reset_index()

st.subheader("Amount by Category")
fig = px.bar(summary, x='category', y='amount', title='Amount by Category')
st.plotly_chart(fig)

# Interactive filtering
category = st.sidebar.selectbox("Category Filter", df['category'].unique())
filtered_df = df[df['category'] == category]
st.subheader(f"Filtered Data: {category}")
st.dataframe(filtered_df)



