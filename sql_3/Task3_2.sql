select item, count(*) as count, round(avg(amount),2) as avg_amount
from orders
group by item
order by count desc, avg_amount desc;