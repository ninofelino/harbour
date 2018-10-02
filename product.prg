local jumlah:=10,x:=0
set print to "product_template.sql"
set print on
set defa to "/home/server/posserver/ics/DAT"
USE "INV.DBF" SHARED

//goto 2250
do while x<1000
x=X+1
IF LEN(rtrim(INV->CODE))>1
? "insert into product_template(ID,Name,sequence,type,categ_id,uom_id,uom_po_id,responsible_id,tracking,sale_line_warn,purchase_line_warn,active,purchase_ok)"
?? " values("
?? RTRIM(INV->CODE)
?? ","
?? "'"
?? strTran(RTRIM(INV->DESC1),"'"," ")
?? "'"
?? ",1,'consu',1,1,1,1,'none','no-message','no-message'"
?? ",TRUE,TRUE) "
? "on CONFLICT ON CONSTRAINT product_template_pkey  DO UPDATE set default_code='"+rtrim(inv->code)+"';"


?  "INSERT INTO product_product (product_tmpl_id,default_code,active) "
?? "VALUES (" + INV->CODE+ ",'" + "1" + "',TRUE) on CONFLICT ON CONSTRAINT product_product_pkey DO UPDATE set active=TRUE;"
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