CREATE TABLE IF NOT EXISTS data_2023_feb (
    event_time TIMESTAMP,
    event_type TEXT,
    product_id INTEGER,
    price FLOAT,
    user_id INTEGER,
    user_session UUID
);

COPY data_2023_feb FROM '/goinfre/tde-raev/DataScience/DataScience_01_DataWarehouse/data_2023_feb.csv' DELIMITER ',' CSV HEADER;
