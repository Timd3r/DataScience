CREATE TABLE customers_joined AS
SELECT 
    c.*, 
    i.category_id, 
    i.category_code, 
    i.brand
FROM customers c
LEFT JOIN items i ON c.product_id = i.product_id;

DROP TABLE customers;
ALTER TABLE customers_joined RENAME TO customers;