#SELECT * FROM sakila.customer;
select * from  customer where store_id=2
SELECT 
    c.customer_id AS CustomerID,
    CONCAT(c.first_name, ' ', c.last_name) AS CustomerName,
    COUNT(r.rental_id) AS RentalCount
FROM customer c
LEFT JOIN rental r ON c.customer_id = r.customer_id
GROUP BY c.customer_id, c.first_name, c.last_name
ORDER BY RentalCount DESC;