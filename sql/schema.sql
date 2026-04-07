-- CUSTOMERS
CREATE TABLE customers_raw (
    customer_id TEXT PRIMARY KEY,
    customer_zip_code_prefix INT,
    customer_city TEXT,
    customer_state TEXT
);

-- ORDERS
CREATE TABLE orders_raw (
    order_id TEXT PRIMARY KEY,
    customer_id TEXT,
    order_status TEXT,
    order_purchase_timestamp TIMESTAMP,
    order_approved_at TIMESTAMP,
    order_delivered_timestamp TIMESTAMP,
    order_estimated_delivery_date TIMESTAMP
);

-- ORDER ITEMS (FIXED STRUCTURE)
CREATE TABLE order_items_raw (
    order_id TEXT,
    product_id TEXT,
    seller_id TEXT,
    price FLOAT,
    shipping_charges FLOAT
);

-- PAYMENTS
CREATE TABLE payments_raw (
    order_id TEXT,
    payment_sequential INT,
    payment_type TEXT,
    payment_installments INT,
    payment_value FLOAT
);

-- CLEAN TABLE
CREATE TABLE orders_clean (
    order_id TEXT,
    customer_id TEXT,
    order_status TEXT,
    order_purchase_timestamp TIMESTAMP
);

-- ANALYTICS TABLE
CREATE TABLE customer_ltv (
    customer_id TEXT,
    total_spent FLOAT
);