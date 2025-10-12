import yfinance as yf
import pandas as pd

def extract_stock_data(ticker_symbol, period="max"):
    """
    Extracts historical stock data using yfinance.
    
    Parameters:
    - ticker_symbol (str): The stock ticker symbol (e.g., 'AAPL' for Apple).
    - period (str): The period for historical data (e.g., '1d', '1mo', '1y', 'max').
    
    Returns:
    - pd.DataFrame: Historical stock data with reset index.
    """
    
    stock_ticker = yf.Ticker(ticker_symbol)
    
    stock_data = stock_ticker.history(period=period)
    
 
    stock_data.reset_index(inplace=True)
    
    return stock_data


apple_data = extract_stock_data("AAPL", period="5y")


print(apple_data.head())
