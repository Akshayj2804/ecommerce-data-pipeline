CREATE TABLE customers_raw (
    customer_id INT,
    name TEXT,
    city TEXT
);

CREATE TABLE products_raw (
    product_id INT,
    name TEXT,
    price FLOAT
);

CREATE TABLE orders_raw (
    order_id INT,
    customer_id INT,
    product_id INT,
    quantity INT,
    order_date DATE
);