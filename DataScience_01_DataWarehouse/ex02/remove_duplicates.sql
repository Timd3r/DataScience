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

DROP TABLE customers;

ALTER TABLE customers_nodup RENAME TO customers;