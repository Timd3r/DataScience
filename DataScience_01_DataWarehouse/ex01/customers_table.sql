COPY data_2022_dec FROM '/tmp/customer/data_2022_dec.csv' WITH (FORMAT csv, HEADER true);

CREATE TABLE IF NOT EXISTS customers AS
    SELECT * FROM data_2022_oct
    UNION ALL
    SELECT * FROM data_2022_nov
    UNION ALL
    SELECT * FROM data_2023_jan
    UNION ALL
    SELECT * FROM data_2022_dec;
