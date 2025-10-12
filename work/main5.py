import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

def plot_tesla_stock(period="5y", save_plot=False):
    """
    Fetches historical TSLA stock data and plots the closing price over time.
    
    Parameters:
    - period (str): Time period (e.g., '1y', '5y', 'max'—default '5y').
    - save_plot (bool): If True, saves the plot as 'tesla_stock_plot.png'.
    
    Returns:
    - None: Displays the plot.
    """

    tsla = yf.Ticker("TSLA")
    
    
    stock_data = tsla.history(period=period)
    
    if stock_data.empty:
        print("No data fetched. Check ticker or period.")
        return
    
    
    plt.figure(figsize=(12, 6))  
    plt.plot(stock_data.index, stock_data['Close'], label='TSLA Close Price', color='blue', linewidth=1.5)

    plt.title(f'Tesla (TSLA) Stock Closing Price - Last {period}', fontsize=16, fontweight='bold')
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Price (USD)', fontsize=12)
    plt.legend()
    plt.grid(True, alpha=0.3)  
    plt.xticks(rotation=45) 
    
    plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x:,.0f}'))
    
    plt.tight_layout()
    

    plt.show()
  
    if save_plot:
        filename = f'tesla_stock_plot_{period.replace("y", "y").replace("max", "max")}.png'
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        print(f"Plot saved as '{filename}'")

plot_tesla_stock(period="5y", save_plot=True)
