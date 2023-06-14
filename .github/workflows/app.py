
#IMPORTING LIBRARIES
import pandas as pd
import numpy as np
import datetime
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

#LOADING DATAFRAMES
#Imports the daily aggregated receipts_daily_df
%cd Downloads/
receipts_daily_df = pd.read_csv('receipts_daily_df.csv')

#Change the types of both dates columns, to be able to use them as the key for the merge
receipts_daily_df["receipt_open_day"] = pd.to_datetime(receipts_daily_df['receipt_open_day'])

#CREATING GRAPHS
weekly_sales_fig = px.box(receipts_daily_df,x="receipt_open_weekday",y="daily_sales",points="all",
       category_orders={"receipt_open_weekday":['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']},
       color='receipt_open_weekday',title="Daily Sales per Day of Week")
weekly_sales_fig.show()

#CREATING SCORECARDS
score_card = go.Figure(go.Indicator(
    mode = "number+delta",
    value = 400,
    number = {'prefix': "$"},
    delta = {'position': "top", 'reference': 320},
    domain = {'x': [0, 1], 'y': [0, 1]}))

#CONFIGURING WEB APP
# Specify the title and logo for the web page
st.set_page_config(page_title='Buhrs Butchershop Sales Prediction',
                   page_icon='logo.png',
                   layout="wide")

# Add a sidebar to the page
## Sidebar Configuration
with st.sidebar:
  st.image('logo.png', output_format="PNG")
  st.title('Buhrs Weekly Sales Forecast')
  st.markdown('')
  st.markdown('Based on Sales Data from May 2020 - March 2023')

  st.sidebar.markdown('---')
  st.sidebar.write("Developed by Buhr's Data Analyst Team")
  st.sidebar.write('Contact at data_deparatment@buhrs.com')

# Specify title of the page
st.title('Weekly Sales Forecast Model')
st.markdown('---')

# Specify sub-header of the page
st.header("Next Week's Predictions")
col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
with col1:
  st.subheader('')
  st.markdown('')
  st.markdown('')
  st.markdown('')
  st.markdown("<style>h4 { font-size: 18px; }</style>", unsafe_allow_html=True)
  st.markdown("<h4>Sales</h4>", unsafe_allow_html=True)
  st.markdown('')
  st.markdown('')
  st.markdown('')
  st.markdown("<h4>Customers</h4>", unsafe_allow_html=True)
  st.markdown('')
  st.markdown('')
  st.markdown('')
  st.markdown("<h4>Avg Receipt</h4>", unsafe_allow_html=True)

with col2:
  st.subheader("MON")
  st.subheader('')
  st.markdown('')
  st.markdown('')
  st.markdown('')
  st.plotly_chart(score_card)

with col3:
  st.subheader("TUES")
  st.subheader('')
  st.markdown('')
  st.markdown('')
  st.markdown('')

with col4:
  st.subheader("WED")
  st.subheader('')
  st.markdown('')
  st.markdown('')
  st.markdown('')

with col5:
  st.subheader("THUR")
  st.subheader('')
  st.markdown('')
  st.markdown('')
  st.markdown('')

with col6:
  st.subheader("FRI")
  st.subheader('')
  st.markdown('')
  st.markdown('')
  st.markdown('')

with col7:
  st.subheader("SAT")
  st.subheader('')
  st.markdown('')
  st.markdown('')
  st.markdown('')

#Specify sub-header of the page
st.markdown('')
st.header("Sales Forecast")
st.plotly_chart(weekly_sales_fig,use_container_width=True)

#Specify sub-header of the page
st.markdown('')
st.header("Customers Forecast")
st.plotly_chart(weekly_sales_fig,use_container_width=True)
