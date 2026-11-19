import pandas as pd
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "data" / "market_data.db"

def create_database():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor() #Allows us to execute SQL commands

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS crypto_prices (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        coin_id TEXT NOT NULL,
        name TEXT NOT NULL,
        symbol TEXT NOT NULL,
        price_usd REAL NOT NULL,
        market_cap_usd REAL,
        volume_24h_usd REAL,
        last_updated TEXT NOT NULL,
        fetched_at TEXT DEFAULT CURRENT_TIMESTAMP,
        UNIQUE(coin_id, last_updated)
    )
""")
    conn.commit()
    conn.close()

def save_market_data(df):

    if df.empty:
        print("No Market Data!!!")
        return

    records_df = df.copy()
    records_df["last_updated"] = records_df["last_updated"].astype(str) #Pandas timestamps into strings
    records = records_df.to_dict(orient="records") #converts each DataFrame row into a dictionary

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    sql = """
        INSERT OR IGNORE INTO crypto_prices (
            coin_id,
            name,
            symbol,
            price_usd,
            market_cap_usd,
            volume_24h_usd,
            last_updated
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """
    rows = [
        (
            record["coin_id"],
            record["name"],
            record["symbol"],
            record["price_usd"],
            record["market_cap_usd"],
            record["volume_24h_usd"],
            record["last_updated"]
        )
        for record in records
    ]

    cursor.executemany(sql, rows) #Insert all records to DB in one operation
    conn.commit()
    conn.close()

    print(f"Successfully saved {cursor.rowcount} records!")


def read_market_data():
    conn = sqlite3.connect(DB_PATH)
    query = """
        SELECT *
        FROM crypto_prices
        ORDER BY fetched_at DESC
    """
    cursor = conn.cursor()
    cursor.execute(query)

    records = cursor.fetchall()

    columns = [description[0] for description in cursor.description]

    conn.close()

    df = pd.DataFrame(records , columns=columns)

    return df
