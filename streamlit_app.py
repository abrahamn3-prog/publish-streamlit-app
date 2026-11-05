import streamlit as st
import pandas as pd

st.title("Advertising and Sales Explorer")

df = pd.read_csv("Advertising_F.csv")

st.subheader("Data preview")
st.dataframe(df.head())

all_cities = sorted(df["City"].unique())
cities = st.multiselect("Choose cities", all_cities, default=all_cities)
filtered = df[df["City"].isin(cities)]

channel = st.selectbox("Choose an advertising channel", ["TV", "radio", "newspaper"])
st.subheader(f"{channel} spend vs. sales")
st.scatter_chart(filtered, x=channel, y="sales")

st.subheader("Average sales by city")
st.bar_chart(filtered.groupby("City")["sales"].mean())

st.subheader("Where the data comes from")
st.map(filtered, latitude="latitude", longitude="longitude")
