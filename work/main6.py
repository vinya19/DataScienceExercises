import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Function to fetch and plot GameStop stock data
def plot_gme_stock(period="5y", save_plot=False):
    """
    Fetches historical GME stock data and plots the closing price over time.
    
    Parameters:
    - period (str): Time period (e.g., '1y', '5y', 'max'—default '5y').
    - save_plot (bool): If True, saves the plot as 'gme_stock_plot.png'.
    
    Returns:
    - None: Displays the plot.
    """
    # Create Ticker for GameStop
    gme = yf.Ticker("GME")
    
    # Fetch historical data
    stock_data = gme.history(period=period)
    
    if stock_data.empty:
        print("No data fetched. Check ticker or period.")
        return
    
    # Plot closing price
    plt.figure(figsize=(12, 6))  # Set figure size
    plt.plot(stock_data.index, stock_data['Close'], label='GME Close Price', color='red', linewidth=1.5)
    
    # Customize the plot
    plt.title(f'GameStop (GME) Stock Closing Price - Last {period}', fontsize=16, fontweight='bold')
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Price (USD)', fontsize=12)
    plt.legend()
    plt.grid(True, alpha=0.3)  # Add light grid
    plt.xticks(rotation=45)  # Rotate x-axis labels for readability
    
    # Format y-axis to show currency
    plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x:,.0f}'))
    
    # Tight layout to prevent clipping
    plt.tight_layout()
    
    # Display the plot
    plt.show()
    
    # Optional: Save to file
    if save_plot:
        filename = f'gme_stock_plot_{period.replace("y", "y").replace("max", "max")}.png'
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        print(f"Plot saved as '{filename}'")

# Example usage: Plot GameStop stock for the last 5 years
plot_gme_stock(period="5y", save_plot=True)

# Optional: For a full OHLC plot (more advanced, requires mplfinance)
# pip install mplfinance
# import mplfinance as mpf
# mpf.plot(stock_data.tail(200), type='candle', style='charles', title='GME Candlestick (Last 200 Days)', volume=True)
