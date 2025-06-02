-- Top 5 customers by total amount spent

SELECT
    c.name AS customer_name,
    SUM(oi.quantity * p.price) AS total_spent
FROM
    customers c
JOIN
    "orders" o ON c.id = o.customer_id
JOIN
    order_items oi ON o.id = oi.order_id
JOIN
    products p ON oi.product_id = p.id
GROUP BY
    c.name
ORDER BY
    total_spent DESC
LIMIT 5;

-- Number of orders placed by each customer
SELECT
    c.name AS customer_name,
    COUNT(o.id) AS number_of_orders
FROM
    customers c
LEFT JOIN
    "orders" o ON c.id = o.customer_id
GROUP BY
    c.name
ORDER BY
    number_of_orders DESC;

-- Products that have never been ordered
SELECT
    p.name AS product_name,
    p.category,
    p.price
FROM
    products p
LEFT JOIN
    order_items oi ON p.id = oi.product_id
WHERE
    oi.product_id IS NULL;