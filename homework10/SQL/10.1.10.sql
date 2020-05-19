select gender,GROUP_CONCAT(`name`) as name
from students 
group by gender 