CREATE TABLE IF NOT EXISTS items (
    product_id INTEGER,
    category_id BIGINT,
    category_code VARCHAR(255),
    brand VARCHAR(255)
);

COPY items FROM '/goinfre/tde-raev/DataScience/DataScience_00_DataEngineer/subject/item/item.csv' WITH (FORMAT csv, HEADER true, DELIMITER ',');
