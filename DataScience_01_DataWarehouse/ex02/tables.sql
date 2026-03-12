CREATE TABLE IF NOT EXISTS data_2022_oct (
    event_time TIMESTAMP,
    event_type TEXT,
    product_id INTEGER,
    price FLOAT,
    user_id BIGINT,
    user_session UUID
);

COPY data_2022_oct FROM '/tmp/customer/data_2022_oct.csv' WITH (FORMAT csv, HEADER true);

CREATE TABLE IF NOT EXISTS data_2022_nov (
    event_time TIMESTAMP,
    event_type TEXT,
    product_id INTEGER,
    price FLOAT,
    user_id BIGINT,
    user_session UUID
);

COPY data_2022_nov FROM '/tmp/customer/data_2022_nov.csv' WITH (FORMAT csv, HEADER true);

CREATE TABLE IF NOT EXISTS data_2023_jan (
    event_time TIMESTAMP,
    event_type TEXT,
    product_id INTEGER,
    price FLOAT,
    user_id BIGINT,
    user_session UUID
);

COPY data_2023_jan FROM '/tmp/customer/data_2023_jan.csv' WITH (FORMAT csv, HEADER true);

CREATE TABLE IF NOT EXISTS data_2022_dec (
    event_time TIMESTAMP,
    event_type TEXT,
    product_id INTEGER,
    price FLOAT,
    user_id BIGINT,
    user_session UUID
);

COPY data_2022_dec FROM '/tmp/customer/data_2022_dec.csv' WITH (FORMAT csv, HEADER true);

CREATE TABLE IF NOT EXISTS customers AS
    SELECT * FROM data_2022_oct
    UNION ALL
    SELECT * FROM data_2022_nov
    UNION ALL
    SELECT * FROM data_2023_jan
    UNION ALL
    SELECT * FROM data_2022_dec;

CREATE TABLE customers_nodup AS
WITH sorted_data AS (
    SELECT *,
        LAG(event_time) OVER (
            PARTITION BY event_type, product_id, price, user_id, user_session 
            ORDER BY event_time
        ) AS prev_event_time
    FROM customers
)
SELECT 
    event_time, 
    event_type, 
    product_id, 
    price, 
    user_id, 
    user_session
FROM sorted_data
WHERE prev_event_time IS NULL 
   OR event_time > prev_event_time + INTERVAL '1 second';