# Importing libraries
import streamlit as st
import pandas as pd
import yfinance as yf
import datetime
import pandas_datareader.data as web
import capm_functions

def get_sp500_tickers():
    table = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    df = table[0]
    stockdata = df['Symbol'].to_list()
    return stockdata

st.set_page_config(page_title = 'CAPM: Expected Return Calculator',
                   page_icon = 'chart_with_upwards_trend',
                   layout = 'wide')

st.title('Capital Asset Pricing Model')
st.markdown('##### Made by [Manmeet Kaur Baxi](https://manmeetkaurbaxi.com)')
st.caption("The Capital Asset Pricing Model(CAPM) is a formula that helps investors calculate how much risk they're taking when they invest in a stock, based on the risk-free rate, the equity risk premium, and the stock's beta. It is a finance model that establishes a linear relationship between the required return on an investment and risk.")
st.caption("Assumed risk free return = 4.5%")

# Getting input from user
tickers = get_sp500_tickers()

col1,col2=st.columns([1,1])
with col1:
    stocklist = st.multiselect('Choose 4 stocks', (tickers),['AAPL','GOOGL','AMZN','NVDA','FANG'])
with col2:
    year_input = st.number_input('Number of years',1,30)

# Download data for S&P500:
try:
    end = datetime.date.today()
    start = datetime.date(datetime.date.today().year-year_input, datetime.date.today().month, datetime.date.today().day)
    sp500 = web.DataReader(['sp500'],'fred',start,end)

    stocks_df = pd.DataFrame()
    for stock in stocklist:
        stock_data = yf.download(stock, period=f'{year_input}y')
        stocks_df[f'{stock}'] = stock_data['Close']

    stocks_df.reset_index(inplace=True)
    sp500.reset_index(inplace=True)

    sp500.columns = ['Date','SP500']
    stocks_df['Date'] = pd.to_datetime(stocks_df['Date']).dt.tz_localize(None)

    stocks_df = pd.merge(stocks_df, sp500, on='Date', how = 'inner')

    # col1, col2 = st.columns([1,1])
    # with col1:
    #     st.markdown('### Dataframe head')
    #     st.dataframe(stocks_df.head(), use_container_width=True,hide_index=True)
    # with col2:
    #     st.markdown('### Dataframe tail')
    #     st.dataframe(stocks_df.tail(), use_container_width=True,hide_index=True)
        
    col1, col2 = st.columns([1,1])
    with col1:
        st.markdown('### Price of all the stocks')
        st.plotly_chart(capm_functions.interactive_plot(stocks_df))
    with col2:
        st.markdown('### Price of all the stocks after normalization')
        st.plotly_chart(capm_functions.interactive_plot(capm_functions.normalize(stocks_df)))

    stocks_daily_return = capm_functions.daily_return(stocks_df)

    beta, alpha = {}, {}

    for i in stocks_daily_return.columns:
        if i != 'Date' and i!= 'SP500':
            b,a = capm_functions.calculate_beta(stocks_daily_return, i)
            beta[i], alpha[i] = b, a
            
    beta_df = pd.DataFrame(columns=['Stock','Beta Value'])
    beta_df['Stock'] = beta.keys()
    beta_df['Beta Value'] = [str(round(i, 2)) for i in beta.values()]

    with col1:
        st.markdown('### Calculated Beta Values')
        st.dataframe(beta_df, use_container_width=True,hide_index=True)

    risk_free_asset = 0
    market_return = stocks_daily_return['SP500'].mean() * 252

    return_df = pd.DataFrame()
    return_value = []
    for stock, value in beta.items():
        return_value.append(risk_free_asset + value * (market_return - risk_free_asset))
    return_df['Stock'] = stocklist
    return_df['Return Value'] = return_value

    with col2:
        st.markdown('### Calculated Return using CAPM')
        st.dataframe(return_df, use_container_width=True,hide_index=True)
        
except:
    st.error('Please select a valid ticker and try again.')