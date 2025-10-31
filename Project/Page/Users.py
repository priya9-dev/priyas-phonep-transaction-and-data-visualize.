import streamlit as st
import pandas as pd
import plotly.express as px

user_df = pd.read_csv("users.csv")
st.title("User Breakdown")

state_choice = st.selectbox("Choose State", user_df['state'].unique())
year_choice = st.selectbox("Choose Year", user_df['year'].unique())

filtered = user_df[(user_df["state"] == state_choice) & (user_df["year"] == year_choice)]

st.subheader(f"User Data for {state_choice}, {year_choice}")
st.dataframe(filtered)

# Treemap
fig1 = px.treemap(filtered, path=['user_type'], values='user_count', title="User Type Treemap")
st.plotly_chart(fig1)

# Choropleth example for user counts, if location columns exist
if 'district' in filtered:
    fig2 = px.choropleth_mapbox(filtered, geojson='district_geojson.json',
        locations='district', color='user_count',
        mapbox_style="carto-positron", zoom=4, center={"lat": 22, "lon": 78},
        title="User Density by District")
    st.plotly_chart(fig2)
