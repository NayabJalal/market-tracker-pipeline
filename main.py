from src.api import fetch_market_data
from src.data_cleaner import clean_market_data

coins = ["btc-bitcoin", "eth-ethereum"]
data = fetch_market_data(coins)
df = clean_market_data(data)

print("\nCleaned Market Data:")
print(df)