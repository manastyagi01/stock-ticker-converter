# Stock Ticker Converter

A Python script to convert Indian stock names into their corresponding ticker symbols using NSE (National Stock Exchange) data.

## Features
- Converts company names to NSE ticker symbols
- Handles bulk conversion through CSV files
- Supports Indian stock market listings
- No API key required

## Setup

1. Clone the repository:
```bash
git clone https://github.com/manastyagi01/stock-ticker-converter.git
cd stock-ticker-converter
```

2. Create and activate virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # For Unix/MacOS
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Add your stock names to `input.csv` file:
```csv
Stock Name
HDFC Bank Limited
Reliance Industries Limited
```

2. Run the script:
```bash
python main.py
```

3. Check `output.csv` for the results:
```csv
Stock Name,Ticker
HDFC Bank Limited,HDFCBANK.NS
Reliance Industries Limited,RELIANCE.NS
```

## Dependencies
- pandas
- requests
- beautifulsoup4

## Notes
- The script uses NSE India data to fetch ticker symbols
- If a ticker symbol is not found, it will return "Not Found"
- Rate limiting is implemented to avoid connection issues