set print to "product_template.sql"
set print on
set defa to "/home/server/posserver/ics/DAT"
USE "INV.DBF" SHARED

do while .not. eof()
IF LEN(INV->CODE)>1
? "insert into product_template(ID,Name,sequence,type,categ_id,uom_id,uom_po_id,responsible_id,tracking,sale_line_warn,purchase_line_warn)"
?? " values("
?? periksa(INV->CODE)
?? ","
?? "'"
?? strTran(RTRIM(INV->DESC1),"'"," ")
?? "'"
?? ",1,'consu',1,1,1,1,'none','no-message','no-message'"
?? ") on CONFLICT ON CONSTRAINT product_template_pkey DO NOTHING;"
ENDIF
skip
enddo
set print to
set print off

function periksa(isi)
    if isi=""
        isi="000" 
    endif
return rtrim(isi)    