CREATE TABLE IF NOT EXISTS data_2022_oct (
    event_time TIMESTAMP,
    event_type TEXT,
    product_id INTEGER,
    price FLOAT,
    user_id BIGINT,
    user_session UUID
);

COPY data_2022_oct FROM '/subject/customer/data_2022_oct.csv' WITH (FORMAT csv, HEADER true);