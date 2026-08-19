# Write your MySQL query statement below
select s.name 
from SalesPerson as s
left join Orders as o
on s.sales_id=o.sales_id
left join Company as c
on o.com_id=c.com_id AND c.name = 'RED'
GROUP BY s.sales_id, s.name
HAVING COUNT(c.com_id) = 0;