select article,last_elem(string_to_array(article,' ')),
replace(article,last_elem(string_to_array(article,' ')),'') 

from inv ;


select a.barcode as id ,(select min(barcode) from inv where article=a.article) as product_tmpl_id,
a.barcode as barcode,a.barcode as default_code
from inv a
order by barcode