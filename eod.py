import psycopg2
#conn = psycopg2.connect("host='localhost' dbname='admin' user='postgres' password='novellina'")
conn = psycopg2.connect("host='192.168.1.36' dbname='odoo' user='postgres' password='odo'")

cursor=conn.cursor()
from dbfread import DBF
# for record in DBF('/home/server/Downloads/INV-HO.DBF',encoding='iso-8859-1'):
   # print(record)
for item in DBF('/home/server/Downloads/INV-HO.DBF',encoding='iso-8859-1'):
    #  print item[1]  
    #  print  list(item.values())
     # print len(item),
     # print item['CODE'],item['DESC1'],item['LQOH']
      statement =" INSERT INTO inv(barcode,article,ukuran)" \
      +" values("+item['CODE']+",'"+item['DESC1'].replace("'","")+"','S'"+")" \
      +" ON CONFLICT ON CONSTRAINT  inv_pkey DO NOTHING"
      if item['CODE'].strip() is None:
         print "Null"
      else:
         cursor.execute(statement)
      conn.commit() 
      


      statement =" INSERT INTO product_attribute_line(id,product_tmpl_id,attribute_id) values("+item['CODE']+","+item['CODE']+",1)"
     # cursor.execute(statement)
     # conn.commit() 
         

      statement =" INSERT INTO product_template(id,name,sequence,type,rental,categ_id,list_price,sale_ok,purchase_ok,uom_id,uom_po_id,company_id,active,responsible_id,sale_line_warn,tracking,purchase_line_warn"\
      ") VALUES ("\
      +item['CODE']+",'"+item['DESC1'].replace("'","")+"',1,'consu',False,1,"+str(item['COSTPRC'])+",True,True,1,1,1,True,1,'no-message','none','no-message') ON CONFLICT ON CONSTRAINT product_template_pkey DO Update set sale_ok=True,available_in_pos=True,list_price="+str(item['SELLPRC'])+" ;"
      
     # print item['DESC1']
      cursor.execute(statement)
      conn.commit() 
      #print statement
      statement = " INSERT INTO product_product(id,product_tmpl_id,active,barcode,create_uid,write_uid)"\
      +" values("+item['CODE']+","+item['CODE']+",True,"+item['CODE']+",1,1) ON CONFLICT ON CONSTRAINT product_product_pkey DO UPDATE SET barcode='"+item['CODE']+"',default_code='"+item['CODE']+"';"
      print statement
      cursor.execute(statement)
      conn.commit() 
      