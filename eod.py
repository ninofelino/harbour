import psycopg2
conn = psycopg2.connect("host='localhost' dbname='odoo' user='postgres' password='novellina'")
cursor=conn.cursor()
from dbfread import DBF
# for record in DBF('/home/server/Downloads/INV-HO.DBF',encoding='iso-8859-1'):
   # print(record)
for item in DBF('/home/server/Downloads/INV-HO.DBF',encoding='iso-8859-1'):
    #  print item[1]  
    #  print  list(item.values())
     # print len(item),
      print item['CODE'],item['DESC1'],item['LQOH']
      statement =" INSERT INTO product_template(id,name,sequence,type,rental,categ_id,list_price,sale_ok,purchase_ok,uom_id,uom_po_id,company_id,active,responsible_id,sale_line_warn,tracking,purchase_line_warn"\
      ") VALUES ("\
      +item['CODE']+",'"+item['DESC1'].replace("'","")+"',1,'consu',False,1,"+str(item['COSTPRC'])+",True,True,1,1,1,True,1,'no-message','none','no-message') ON CONFLICT ON CONSTRAINT product_template_pkey DO Update set sale_ok=True;"
      
     # print item['DESC1']
      cursor.execute(statement)
      conn.commit() 
      print statement
    