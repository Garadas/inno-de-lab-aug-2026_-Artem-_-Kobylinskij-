select concat(c.first_name, ' ', c.last_name) as full_name, c.country, 
	count(o.order_id) as total_orders,
	sum(o.amount) as total_amount
from customers as c
join orders as o on o.customer_id = c.customer_id
where exists (
    select * from shippings s 
    where s.customer = c.customer_id 
    	and s.status = 'Delivered'
)
group by c.customer_id, c.first_name, c.last_name, c.country
having count(o.order_id) >= 2
order by total_amount desc;