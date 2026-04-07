import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import psycopg2
from config import DB_CONFIG

def run():
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()

    print("Running validation checks...")

    cur.execute("SELECT COUNT(*) FROM orders_raw WHERE customer_id IS NULL;")
    print("Null customer_id:", cur.fetchone()[0])

    cur.execute("SELECT COUNT(*) FROM order_items_raw WHERE price <= 0;")
    print("Invalid price count:", cur.fetchone()[0])

    conn.close()

if __name__ == "__main__":
    run()