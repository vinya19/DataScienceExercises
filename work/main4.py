import requests
from bs4 import BeautifulSoup
import pandas as pd
import time  

def scrape_gme_revenue(url="https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue"):
    """
    Scrapes annual revenue data for GameStop (GME) from Macrotrends.net.
    
    Parameters:
    - url (str): The URL to scrape (default is GME's revenue page).
    
    Returns:
    - pd.DataFrame: DataFrame with columns like 'Year' and 'Revenue (Billions USD)'.
    
    Note: Targets the annual revenue table. Uses headers to mimic a browser if blocked.
    """

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
    
        response = requests.get(url, headers=headers)
        response.raise_for_status()      
    
        soup = BeautifulSoup(response.content, 'lxml')

        table = soup.find('table', class_='historical_data_table')
        if not table:
            raise ValueError("Revenue table not found. Site structure may have changed.")
        
        
        rows = table.find_all('tr')
        data = []
        
        for row in rows[1:]:  
            cols = row.find_all('td')
            if len(cols) >= 2:
                year = cols[0].text.strip()
                revenue = cols[1].text.strip().replace('$', '').replace(',', '')  # Clean revenue string
                data.append({'Year': year, 'Revenue (Billions USD)': float(revenue)})
        
    
        df = pd.DataFrame(data)
        df['Revenue (Billions USD)'] = pd.to_numeric(df['Revenue (Billions USD)'], errors='coerce')
        
        df = df.sort_values('Year', ascending=False).reset_index(drop=True)
        
        return df
    
    except requests.RequestException as e:
        print(f"Error fetching page: {e}")
        return None
    except Exception as e:
        print(f"Error parsing data: {e}")
        return None

gme_revenue = scrape_gme_revenue()

if gme_revenue is not None:
    
    print(gme_revenue.head(10))  
    
    
    gme_revenue.to_csv("gme_annual_revenue.csv", index=False)
    print("\nData saved to 'gme_annual_revenue.csv'")
else:
    print("Failed to scrape data. Check your internet connection or site changes.")


time.sleep(1)
