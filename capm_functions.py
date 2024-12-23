import plotly.express as px
import numpy as np

def interactive_plot(df):
    '''
    Function to create a line plot of all the tickers selected for the given timeframe
    '''
    fig = px.line()
    for i in df.columns[1:]:
        fig.add_scatter(x=df['Date'], y=df[i], name = i)
    fig.update_layout(autosize=True, width=1420, margin=dict(l=20, r=20, t=50, b=20), legend=dict(orientation='h',yanchor='bottom',y=1.02,xanchor='right',x=1))
    return fig

def normalize(df):
    '''
    Function to normalize the prices based on the initial price
    '''
    normalize_df = df.copy()
    for i in normalize_df.columns[1:]:
        normalize_df[i] = normalize_df[i]/normalize_df[i][0]
    return normalize_df

def daily_return(df):
    '''
    Function to calculate daily return
    '''
    daily_return_df = df.copy()
    for i in df.columns[1:]:
        for j in range(1, len(df)):
            daily_return_df[i][j] = ((df[i][j]-df[i][j-1])/df[i][j-1])*100
        daily_return_df[i][0] = 0
    return daily_return_df

def calculate_beta(stocks_daily_return,stock):
    '''
    Function to calculate beta
    '''
    market_return = stocks_daily_return["SP500"].mean()*252  # 252 is the number of active trading days
    b,a = np.polyfit(stocks_daily_return['SP500'],stocks_daily_return[stock],1)
    return b,a