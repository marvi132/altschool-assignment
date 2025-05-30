-- Top 5 Customers by Total Amount Spent
SELECT 
    c.id AS customer_id,
    c.name AS customer_name,
    SUM(o.quantity * p.price) AS total_spent
FROM 
    order_items o
JOIN 
    orders ord ON o.order_id = ord.id
JOIN 
    customers c ON ord.customer_id = c.id
JOIN 
    products p ON o.product_id = p.id
GROUP BY 
    c.id, c.name
ORDER BY 
    total_spent DESC
LIMIT 5;



-- Number of Orders placed by each Customers
SELECT 
    o.customer_id,
    c.name AS customer_name,
    COUNT(distinct i.order_id) AS number_of_orders
FROM 
    customers c
JOIN 
    orders o ON o.customer_id = c.id
JOIN 
    order_items i ON i.order_id = o.id
GROUP BY 
    o.customer_id, c.name
ORDER BY 
    number_of_orders DESC;



-- Products that have never been ordered
SELECT 
    p.id,
    p.name
FROM 
    products p
LEFT JOIN 
    order_items o ON p.id = o.product_id
WHERE 
    o.product_id IS NULL;



