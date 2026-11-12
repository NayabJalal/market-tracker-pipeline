import requests

#uppercase variable names are a common convention for constants: values that we don't intend to change during program execution.
BASE_URL = "https://api.coinpaprika.com/v1/tickers/"

def fetch_market_data(coin_ids):
    market_data = [] #Empty Python List
    for coin_id in coin_ids:
        url = f"{BASE_URL}{coin_id}" #https://api.coinpaprika.com/v1/tickers/btc-bitcoin
        try: 
            response = requests.get(url, timeout=15)
            
            response.raise_for_status() #Gives HTTP status code
            
            data = response.json() #CoinPaprika returns data in JSON format
            
            usd_data = data["quotes"]["USD"]
            
            coin = {
    "coin_id": data["id"],
    "name": data["name"],
    "symbol": data["symbol"],
    "price_usd": usd_data["price"],
    "market_cap_usd": usd_data["market_cap"],
    "volume_24h_usd": usd_data["volume_24h"],
    "last_updated": data["last_updated"]
}
            market_data.append(coin)
            print(f"Successfully fetched {data['name']}")

        except requests.exceptions.RequestException as e:
            print(f"API request failed for {coin_id}: {e}")

        except (KeyError, ValueError, TypeError) as e:
            print(f"Invalid API response for {coin_id}: {e}")
    return market_data