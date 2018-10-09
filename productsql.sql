select article,last_elem(string_to_array(article,' ')),
replace(article,last_elem(string_to_array(article,' ')),'') 

from inv