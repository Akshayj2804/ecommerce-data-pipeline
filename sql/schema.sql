-- RAW TABLES
CREATE TABLE customers_raw (
    customer_id INT PRIMARY KEY,
    name TEXT,
    city TEXT
);

CREATE TABLE products_raw (
    product_id INT PRIMARY KEY,
    name TEXT,
    price FLOAT
);

CREATE TABLE orders_raw (
    order_id INT PRIMARY KEY,
    customer_id INT,
    product_id INT,
    quantity INT,
    order_date DATE
);

-- CLEAN TABLE
CREATE TABLE orders_clean (
    order_id INT,
    customer_id INT,
    product_id INT,
    quantity INT,
    order_date DATE
);

-- ANALYTICS TABLE
CREATE TABLE customer_ltv (
    customer_id INT,
    total_spent FLOAT
);