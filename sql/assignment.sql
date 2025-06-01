first 5 customers by total amount spent
SELECT c.name as customer_name,SUM(price * quantity) AS total_amount_spent
FROM customers c
JOIN orders o ON o.customer_id = c.id
JOIN order_items oi ON oi.order_id = o.id
JOIN products p ON p.id = oi.product_id
GROUP BY c.name
ORDER BY total_amount_spent DESC
LIMIT 5;

Number of orders placed by each customer
SELECT c.id AS customer_id, c.name AS customer_name,COUNT(o.id) AS number_of_orders
FROM customers c
LEFT JOIN orders o ON c.id = o.customer_id
GROUP BY c.id, c.name
ORDER BY number_of_orders DESC, customer_name;

Products that have never been ordered
SELECT p.name AS product_name
FROM products p
LEFT JOIN order_items oi ON p.id = oi.product_id
WHERE oi.product_id IS NULL;
