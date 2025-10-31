import streamlit as st
import pandas as pd
import plotly.express as px

# Load transaction data
df = pd.read_csv("transactions.csv")  # Columns: date, amount, state, year, quarter, type

st.title("Transaction Data Hotspots & Breakdowns")

# Sidebar Filters
state_sel = st.sidebar.selectbox('Select State', df['state'].unique())
year_sel = st.sidebar.selectbox('Select Year', sorted(df['year'].unique()))
quarter_sel = st.sidebar.selectbox('Select Quarter', sorted(df['quarter'].unique()))

# Filtered Data
filtered = df[
    (df['state'] == state_sel) &
    (df['year'] == year_sel) &
    (df['quarter'] == quarter_sel)
]

st.subheader(f"Transactions in {state_sel}, Year {year_sel}, Q{quarter_sel}")
st.dataframe(filtered)

# Hotspot: Transaction Amount by City
if 'city' in filtered:
    fig_point = px.scatter_mapbox(
        filtered,
        lat="latitude", lon="longitude", size="amount",
        color="amount", hover_name="city", zoom=5,
        mapbox_style="carto-positron",
        title="Transaction Hotspots by City"
    )
    st.plotly_chart(fig_point)

# Breakdown: Transaction Type Distribution
if 'type' in filtered:
    breakdown = filtered.groupby('type')['amount'].sum().reset_index()
    fig_type = px.bar(
        breakdown, x='type', y='amount', color='type',
        title="Transaction Breakdown by Type"
    )
    st.plotly_chart(fig_type)

# Breakdown: Pie Chart Transaction Type
if 'type' in filtered:
    fig_pie = px.pie(
        breakdown, names='type', values='amount',
        title="Transaction Type Proportions"
    )
    st.plotly_chart(fig_pie)



