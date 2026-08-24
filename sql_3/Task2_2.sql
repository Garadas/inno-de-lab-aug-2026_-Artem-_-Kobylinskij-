select s.status, c.first_name, c.last_name 
from shippings as s
join customers as c on s.customer = c.customer_id;