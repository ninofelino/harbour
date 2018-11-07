select row_number()  over(order by t.name) as id,t.name from
(
select mclass as name from inv group by 1 order by 1
) t