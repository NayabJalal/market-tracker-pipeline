from src.api import fetch_market_data
from src.data_cleaner import clean_market_data
from src.database import create_database, save_market_data, read_market_data

coins = ["btc-bitcoin", "eth-ethereum"]

create_database()

data = fetch_market_data(coins)
df = clean_market_data(data)

print("\nCleaned Market Data:")
print(df)

save_market_data(df)

store_df = read_market_data()

print("\nData Retrieved From SQLite:")
print(store_df)