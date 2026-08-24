select first_name, last_name, amount
from customers as c
join orders as o on o.customer_id = c.customer_id
where o.amount = (select max(amount) from orders);
