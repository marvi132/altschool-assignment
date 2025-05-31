--Top 5 customers by total amount spent

select customers.id as customer_id, customers.name as customer_name, sum(order_items.quantity*price) as total_amount 
from customers
inner join orders on customers.id=orders.customer_id
inner join order_items on orders.id=order_items.order_id
inner join products on order_items.product_id=products.id
group by customers.name
order by total_amount desc
limit 5;

-- Number of orders per customer

select customers.id as customer_id, customers.name as customer_name, count(orders.customer_id) as total_order 
from customers
inner join orders on customers.id=orders.customer_id
group by customers.name
order by customer_name;

-- Products that have never been ordered

select products.id as product_id, products.name as unsold_product
from products
left join order_items on products.id=order_items.product_id
where order_items.product_id is null;
