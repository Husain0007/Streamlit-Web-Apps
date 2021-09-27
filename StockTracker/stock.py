import yfinance as yf
import streamlit as st 
import pandas as pd

st.write("""
# Simple Stock Price App
Shown are closing stock price and volume of GameStop!
""")

tickerSymbol = 'GME'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='1d', start= '2019-1-1', end='2021-8-31')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)