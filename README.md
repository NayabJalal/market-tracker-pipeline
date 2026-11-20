# Market Tracker Pipeline

A Python-based cryptocurrency market data pipeline that fetches real-time market information from the CoinPaprika API, cleans and processes the data using Pandas, and stores historical records in an SQLite database.

## Features

- **API Integration:** Fetches cryptocurrency market data using the CoinPaprika API.
- **Data Cleaning:** Uses Pandas to handle missing values, remove duplicates, and convert timestamps.
- **Database Storage:** Stores cryptocurrency market data in an SQLite database.
- **Historical Records:** Maintains historical snapshots using unique coin and timestamp combinations.
- **Data Retrieval:** Reads previously stored market records from SQLite.
- **Logging:** Tracks pipeline activities, warnings, and errors in both the console and a log file.
- **Error Handling:** Handles API and database errors gracefully.
- **Environment Configuration:** Uses environment variables to manage API configuration.

## Tech Stack

- Python
- Pandas
- Requests
- SQLite
- Python-dotenv
- Logging

## Project Structure

```text
market-tracker-pipeline/
│
├── data/
│   └── market_data.db
│
├── logs/
│   └── pipeline.log
│
├── src/
│   ├── api.py
│   ├── config.py
│   ├── data_cleaner.py
│   ├── database.py
│   └── logger.py
│
├── .env.example
├── .gitignore
├── main.py
├── requirements.txt
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/NayabJalal/market-tracker-pipeline.git
cd market-tracker-pipeline
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows:**
```powershell
venv\Scripts\Activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root and add:

```env
API_BASE_URL=https://api.coinpaprika.com/v1/tickers/
```

You can use `.env.example` as a reference.

### 5. Run the pipeline

```bash
python main.py
```

## Database Schema

The pipeline stores data in an SQLite table named `crypto_prices`.

| Column | Description |
|---|---|
| id | Unique record ID |
| coin_id | Cryptocurrency identifier |
| name | Cryptocurrency name |
| symbol | Cryptocurrency symbol |
| price_usd | Current price in USD |
| market_cap_usd | Market capitalization |
| volume_24h_usd | 24-hour trading volume |
| last_updated | Timestamp provided by the API |
| fetched_at | Timestamp when the record was stored |

A unique constraint on `coin_id` and `last_updated` helps prevent duplicate snapshots.

## Data Pipeline

```text
CoinPaprika API
      |
      v
   api.py
      |
      v
data_cleaner.py
      |
      v
  database.py
      |
      v
 SQLite Database
      |
      v
 Historical Data Retrieval
```

Logging and error handling help monitor the pipeline throughout execution.

## Current Scope

The pipeline currently collects market information for Bitcoin and Ethereum. It can be extended to support additional cryptocurrencies and further data analysis.

## Future Improvements

- SQL-based market analysis
- Historical price trend analysis
- Data visualization
- Automated scheduled data collection
- Unit and integration testing

## Author

**Md Nayab**

GitHub: [NayabJalal](https://github.com/NayabJalal)