select order_id, customer_id, item, 
amount, sum(amount) over(partition by customer_id) as total_by_customer
from orders
order by order_id