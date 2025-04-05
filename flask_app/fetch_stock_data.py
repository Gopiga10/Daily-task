import requests
import pandas as pd

# Your MarketStack API Key
API_KEY = "7ce7cf88fb2ed6c9c9ab11d132d42eb2"  # Replace with your actual API key

# API Endpoint (Example: Fetch data for Apple - AAPL)
STOCK_SYMBOL = "AAPL"  # Change to your preferred stock
API_URL = f"http://api.marketstack.com/v1/eod?access_key={API_KEY}&symbols={STOCK_SYMBOL}"

# Make the API request
response = requests.get(API_URL)
data = response.json()

# Check if the API request was successful
if "data" in data:
    # Convert API response to DataFrame
    df = pd.DataFrame(data["data"])

    # Select relevant columns
    df = df[["date", "close"]]

    # Save as CSV
    df.to_csv("data/stock_data.csv", index=False)
    print("Stock data downloaded and saved as stock_data.csv!")
else:
    print("Error fetching data:", data)
