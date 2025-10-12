import yfinance as yf
import pandas as pd

def extract_stock_data(ticker_symbol, period="max", interval="1d"):
    """
    Extracts historical stock data using yfinance.
    
    Parameters:
    - ticker_symbol (str): The stock ticker symbol (e.g., 'TSLA' for Tesla, 'AAPL' for Apple).
    - period (str): The period for historical data (e.g., '1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max').
    - interval (str): The data interval (e.g., '1m' for 1-minute, '1d' for daily—default is '1d').
    
    Returns:
    - pd.DataFrame: Historical stock data with reset index (Date as a column).
    
    Note: Data is adjusted for splits and dividends where applicable.
    """
 
    stock_ticker = yf.Ticker(ticker_symbol)
    
  
    stock_data = stock_ticker.history(period=period, interval=interval)

    stock_data.reset_index(inplace=True)
    
    return stock_data

tesla_data = extract_stock_data("TSLA", period="5y")

print(tesla_data.head())

tesla_ticker = yf.Ticker("TSLA")
print("\nStock Info:")
print(tesla_ticker.info.get('longName', 'N/A'))  
print(f"Current Price: ${tesla_ticker.info.get('currentPrice', 'N/A')}")
print(f"Market Cap: ${tesla_ticker.info.get('marketCap', 'N/A'):,}")
