## Project Overview
The CAPM Financial Analysis project is a Python-based implementation of the Capital Asset Pricing Model (CAPM). This model helps investors estimate the expected return on an investment, considering its inherent risk. 
It leverages factors such as the risk-free rate, the equity risk premium, and the stock's beta to provide insights into potential returns and associated risks.
This application uses libraries like Pandas, NumPy, Streamlit, and Plotly to gather stock data from Yahoo Finance, perform CAPM calculations, and present results in a user-friendly format.

## Background Information
### What is CAPM?
The Capital Asset Pricing Model (CAPM) establishes a relationship between the risk and expected return of a security. It states that the expected return on a security is the sum of the risk-free rate and a risk premium:

Expected Return = Risk-Free Rate + Beta * (Market Return - Risk-Free Rate)

### Key Concepts
1. Risk-Free Asset Return: Represents the return of a theoretically risk-free investment, such as a 10-year US Treasury bill. Investors preferring minimal risk often choose this asset, accepting lower returns in exchange for security.
2. Market Portfolio Return: Represents the market portfolio's average return, comprising all market securities. The S&P 500 index is used as a proxy for market portfolio return in this project.
3. Beta (β): A measure of a stock's sensitivity to market movements. 
    - β = 0: No market sensitivity.
    - β < 1: Low sensitivity to market changes.
    - β = 1: Moves in tandem with the market.
    - β > 1: High sensitivity to market changes.
    - β < 0: Inversely correlated with the market.

## Usage
The CAPM Financial Analysis application simplifies the investment analysis process. Here’s how to use it:
1. Select Stocks by Ticker: 
    - Use the multi-select input to choose one or more stocks by their ticker symbols.
    - The dropdown menu provides a list of available tickers.
2. Specify Investment Duration:
    - Input the number of years you plan to invest.
3. View Results:
    - The application retrieves historical stock prices for the selected stocks and the S&P 500 index.
    - It normalizes stock prices based on initial values and displays the data as an interactive plot.    
    - Beta and alpha values for each stock are calculated from daily returns and shown in a table.    
    - The expected returns for each stock are calculated using the CAPM formula and presented in a results table.
4. Interpret Results:
    - The Normalized Prices Plot visualizes stock performance relative to initial prices.
    - The Beta Values Table highlights each stock's risk relative to the market.
    - The Expected Returns Table provides estimated returns based on the CAPM formula.

## Assumptions
1. Risk-Free Rate: Assumed to be 4.25%.
2. Market Portfolio: The S&P 500 index serves as a benchmark for market returns.
3. Data Sources:
    - Stock price data is fetched using the Yahoo Finance API (via the yfinance library).
    - S&P 500 data is obtained from the FRED database (via the pandas_datareader library).

_Please give a 🌟 if you found this repository helpful in any manner._
