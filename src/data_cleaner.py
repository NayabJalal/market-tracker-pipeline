import pandas as pd

def clean_market_data(market_data):
    df = pd.DataFrame(market_data) #List into Dict
    df = df.dropna() #removes missing values
    df = df.drop_duplicates(subset=["coin_id"])
    df["last_updated"] = pd.to_datetime(
        df["last_updated"], utc=True
    )
    df = df.reset_index(drop=True)
    return df