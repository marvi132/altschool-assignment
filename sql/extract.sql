--- This is the script used for the SQL queries to Extract data

--- Query 1: Top 5 customers by total amount Spent
SELECT
    cust.name as customer_name,
    SUM(oi.quantity * prod.price) as total_amount_spent
FROM
    customers cust
JOIN main.orders o on cust.id = o.customer_id
JOIN main.order_items oi on o.id = oi.order_id
JOIN main.products prod on oi.product_id = prod.id
Group By cust.name
ORDER BY total_amount_spent DESC
LIMIT 5;

--- Query 2: Number of orders per customer
SELECT
    cust.id as customer_id,
    cust.name as customer_name,
    COUNT(o.id) as number_of_orders
FROM
    customers cust
LEFT JOIN main.orders o on cust.id = o.customer_id
GROUP BY cust.name
ORDER BY number_of_orders DESC;

-- Query 3: Products that have never been ordered
SELECT
    prod.id AS product_id,
    prod.name AS product_name,
    prod.category,
    prod.price,
    CASE
        WHEN COUNT(oi.product_id) > 0 THEN 'TRUE' -- If there's at least one order item for this product
        ELSE 'FALSE'                             -- If no order items exist for this product (due to LEFT JOIN)
    END AS has_been_ordered
FROM
    products prod
LEFT JOIN
    order_items oi ON prod.id = oi.product_id
GROUP BY
    prod.id, prod.name, prod.category, prod.price
ORDER BY
    prod.id;


