import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def get_ticker_symbol(stock_name):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        search_url = f"https://www.nseindia.com/api/search/autocomplete?q={stock_name}"
        response = requests.get(search_url, headers=headers)
        data = response.json()
        
        if data and 'symbols' in data and len(data['symbols']) > 0:
            return data['symbols'][0]['symbol']
        
        return f"{stock_name.replace(' ', '').upper()}.NS"
    except Exception as e:
        print(f"Error fetching data for {stock_name}: {e}")
    return "Not Found"

def main():
    input_file = 'input.csv'
    output_file = 'output.csv'

    df = pd.read_csv(input_file)
    tickers = []
    
    for stock_name in df['Stock Name']:
        ticker = get_ticker_symbol(stock_name)
        tickers.append(ticker)
        time.sleep(1)
    
    df['Ticker'] = tickers
    df.to_csv(output_file, index=False)
    print("Ticker symbols have been written to output.csv")

if __name__ == "__main__":
    main()
