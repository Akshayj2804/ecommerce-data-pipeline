import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import psycopg2
from config import DB_CONFIG

def run():
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()

    print("Running transformations...")

    # Clean data
    cur.execute("DELETE FROM orders_clean;")
    cur.execute("""
        INSERT INTO orders_clean
        SELECT * FROM orders_raw
        WHERE customer_id IS NOT NULL;
    """)

    # Analytics
    cur.execute("DELETE FROM customer_ltv;")
    cur.execute("""
        INSERT INTO customer_ltv
        SELECT 
            o.customer_id,
            SUM(p.price * o.quantity) as total_spent
        FROM orders_clean o
        JOIN products_raw p
        ON o.product_id = p.product_id
        GROUP BY o.customer_id;
    """)

    conn.commit()
    conn.close()

    print("Transformations completed.")

if __name__ == "__main__":
    run()