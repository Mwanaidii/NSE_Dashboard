import streamlit as st
import pandas as pd
import seaborn as sns
import plotly_express as px
import matplotlib.pyplot as plt
import streamlit.components.v1 as components
st.set_page_config(layout="wide", initial_sidebar_state="expanded", page_icon=":bar_chart:", page_title='NSE_Dashboard')

path = 'C:/Users/HP\Desktop/Class_Notes/NSE_Dashboard/data.csv'
st.sidebar.header('NSE INTERACTIVE DASHBOARD')

# Check for uploaded dataset.
NSE_Data = pd.read_csv('C:/Users/HP\Desktop/Class_Notes/NSE_Dashboard/data.csv')

##inputting the select options
st.sidebar.header('Please Filter Here:')
Ticker = st.sidebar.selectbox(
    "Select the Ticker Symbol:",
    options=NSE_Data["ticker"].unique()
)


# inputing the start and end date
start = st.sidebar.date_input('start', value=pd.to_datetime('2020-01-01'))
end = st.sidebar.date_input('End', value=pd.to_datetime('today'))
print(NSE_Data.head())

st.title(":bar_chart: Stock Prices Graphs")
st.markdown("##")

##
print(NSE_Data.head())

df = NSE_Data.query("ticker == @Ticker")
fig = px.bar(df, x = df.date, y= df.price, title = Ticker)
st.plotly_chart(fig)


