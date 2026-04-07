import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import psycopg2
from config import DB_CONFIG

def run():
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()

    print("Running transformations...")

    # Clean orders
    cur.execute("DELETE FROM orders_clean;")
    cur.execute("""
        INSERT INTO orders_clean
        SELECT 
            order_id,
            customer_id,
            order_status,
            order_purchase_timestamp
        FROM orders_raw
        WHERE customer_id IS NOT NULL;
    """)

    # Customer Lifetime Value
    cur.execute("DELETE FROM customer_ltv;")
    cur.execute("""
        INSERT INTO customer_ltv
        SELECT 
            o.customer_id,
            SUM(oi.price + oi.shipping_charges) AS total_spent
        FROM orders_clean o
        JOIN order_items_raw oi ON o.order_id = oi.order_id
        GROUP BY o.customer_id;
    """)

    conn.commit()
    conn.close()

    print("Transformations completed.")


if __name__ == "__main__":
    run()