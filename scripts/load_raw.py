import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pandas as pd
import psycopg2
from config import DB_CONFIG

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_csv(file, table):
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()

    file_path = os.path.join(BASE_DIR, file)
    df = pd.read_csv(file_path)

    # Convert datetime columns
    for col in df.columns:
        if "timestamp" in col or "date" in col:
            df[col] = pd.to_datetime(df[col], errors='coerce')

    # Convert NaN + NaT → None
    df = df.astype(object).where(pd.notnull(df), None)

    for _, row in df.iterrows():
        values = tuple(row)
        placeholders = ','.join(['%s'] * len(values))

        try:
            cur.execute(f"INSERT INTO {table} VALUES ({placeholders})", values)
        except psycopg2.errors.UniqueViolation:
            conn.rollback()

    conn.commit()
    conn.close()


def run():
    print("Loading raw data...")

    load_csv("data/raw/customers.csv", "customers_raw")
    load_csv("data/raw/orders.csv", "orders_raw")
    load_csv("data/raw/order_items.csv", "order_items_raw")
    load_csv("data/raw/payments.csv", "payments_raw")

    print("Raw data loaded.")


if __name__ == "__main__":
    run()