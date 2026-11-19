import pandas as pd
import sqlite3
from pathlib import Path
from src.logger import logger

DB_PATH = Path(__file__).resolve().parent.parent / "data" / "market_data.db"


def create_database():

    conn = None

    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
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

        logger.info("Database and crypto_prices table are ready.")

    except sqlite3.Error:
        logger.exception("Failed to create database or table.")
        raise#propagates the error

    finally:
        if conn is not None:
            conn.close()


def save_market_data(df):

    if df.empty:
        logger.warning("No market data available to save.")
        return

    conn = None
    try:
        # Convert DataFrame into records
        records_df = df.copy()
        records_df["last_updated"] = records_df["last_updated"].astype(str)
        records = records_df.to_dict(orient="records")

        # Connect to DB
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        sql = """
            INSERT OR IGNORE INTO crypto_prices (
                coin_id, name, symbol, price_usd,
                market_cap_usd, volume_24h_usd, last_updated
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

        #Insert all records at once
        cursor.executemany(sql, rows)

        conn.commit()

        logger.info(
            f"Successfully saved {cursor.rowcount} records."
        )

    except sqlite3.Error:
        logger.exception("Database error while saving market data.")
        raise

    finally:
        if conn is not None:
            conn.close()


def read_market_data():

    conn = None

    try:
        # Connect to SQLite database
        conn = sqlite3.connect(DB_PATH)

        # Create cursor
        cursor = conn.cursor()

        # Retrieve all records
        query = """
            SELECT *
            FROM crypto_prices
            ORDER BY fetched_at DESC
        """

        cursor.execute(query)

        # Fetch all records
        records = cursor.fetchall()

        # Get column names
        columns = [description[0] for description in cursor.description]

        logger.info(f"Retrieved {len(records)} records from database.")

        # Convert records into DataFrame
        df = pd.DataFrame(records, columns=columns)

        return df

    except sqlite3.Error:
        logger.exception("Failed to retrieve market data.")
        raise

    finally:
        if conn is not None:
            conn.close()

