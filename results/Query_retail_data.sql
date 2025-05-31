-- Top 5 customers by amount spent

select c.name as customer_name,
	SUM(order_items.quantity * products.price) as total_amount_spent
from customers c
join orders o on c.id = o.customer_id
join order_items on o.id = order_items.order_id
join products on order_items.product_id = products.id
group by c.id, c.name
order by total_amount_spent DESC
Limit 5;

-- orders by each customers
Select c.name as customer_name,
    Count(o.id) as number_of_orders
from customers c
join orders o on c.id = o.customer_id
group by c.id, c.name
order by number_of_orders DESC;

-- product that has never been ordered
Select  p.id,
     p.name,
    p.category,
    p.price
from products p
join order_items oi on p.id = oi.product_id
where oi.id is null;

-- For the product not ordered,we get an empty table value because all products have been ordered.