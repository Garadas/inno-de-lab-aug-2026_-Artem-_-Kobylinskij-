select c.first_name, c.last_name, o.item, o.amount 
from orders as o
join customers as c on o.customer_id = c.customer_id;