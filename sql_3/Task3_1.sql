select country, count(*) as count 
from customers
group by country
order by count desc;