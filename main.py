from src.api import fetch_market_data

coins = ["btc-bitcoin", "eth-ethereum"]
data = fetch_market_data(coins)
print("\nFinal Market Data:")
print(data)