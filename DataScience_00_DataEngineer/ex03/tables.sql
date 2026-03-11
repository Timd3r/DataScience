CREATE TABLE IF NOT EXISTS data_2022_oct (
    event_time TIMESTAMP,
    event_type TEXT,
    product_id INTEGER,
    price FLOAT,
    user_id BIGINT,
    user_session UUID
);

COPY data_2022_oct FROM '/goinfre/tde-raev/DataScience/DataScience_00_DataEngineer/subject/customer/data_2022_oct.csv' WITH (FORMAT csv, HEADER true);

CREATE TABLE IF NOT EXISTS data_2022_nov (
    event_time TIMESTAMP,
    event_type TEXT,
    product_id INTEGER,
    price FLOAT,
    user_id BIGINT,
    user_session UUID
);

COPY data_2022_nov FROM '/goinfre/tde-raev/DataScience/DataScience_00_DataEngineer/subject/customer/data_2022_nov.csv' WITH (FORMAT csv, HEADER true);

CREATE TABLE IF NOT EXISTS data_2023_jan (
    event_time TIMESTAMP,
    event_type TEXT,
    product_id INTEGER,
    price FLOAT,
    user_id BIGINT,
    user_session UUID
);

COPY data_2023_jan FROM '/goinfre/tde-raev/DataScience/DataScience_00_DataEngineer/subject/customer/data_2023_jan.csv' WITH (FORMAT csv, HEADER true);

CREATE TABLE IF NOT EXISTS data_2022_dec (
    event_time TIMESTAMP,
    event_type TEXT,
    product_id INTEGER,
    price FLOAT,
    user_id BIGINT,
    user_session UUID
);

COPY data_2022_dec FROM '/goinfre/tde-raev/DataScience/DataScience_00_DataEngineer/subject/customer/data_2022_dec.csv' WITH (FORMAT csv, HEADER true);

