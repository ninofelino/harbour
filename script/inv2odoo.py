import psycopg2
import datetime
conn = psycopg2.connect("host='localhost' dbname='odoo' user='postgres' password='odoo'")
cursor=conn.cursor()
cursor.execute("""SELECT * from invvariant""")
rows = cursor.fetchall()
for row in rows:
    print "   ", row[0]
    statement=" Insert into product_template(id,name,sequence,type,categ_id,uom_id,uom_po_id,responsible_id,tracking,purchase_line_warn,sale_delay,active) "\
    +" values("+row[0]+",'"+row[2]+"',0,'consu',1,1,1,1,'none','no-message',1,True) "\
    +" ON CONFLICT ON CONSTRAINT product_template_pkey DO UPDATE SET active=True,purchase_ok=True,list_price="+str(row[7])+";"
    print row[7]
    #print statement

    cursor.execute(statement)
    conn.commit() 
    jml = row[1]
    if jml > 1 :
               statement=" Insert into Product_product(id,product_tmpl_id,barcode) "\
               +" values("+row[0]+","+row[0]+",'"+row[0]+"') "\
               +"ON CONFLICT ON CONSTRAINT product_product_pkey DO UPDATE SET BARCODE="+row[0]
               cursor.execute(statement)
               conn.commit() 
       # statement=" Insert into Product_attribute_line(id,product_tmpl_id,attribute_id) values("\
       #+row[0]+","+row[0]+",1) ON CONFLICT ON CONSTRAINT product_attribute_line_pkey DO NOTHING;"
       #print statement
       #cursor.execute(statement)
       #conn.commit() 
      
       #print statement
  
cursor.execute("""SELECT * from invproduct_product""")
rows = cursor.fetchall()
for row in rows:     
    #print row[0]
    statement=" Insert into Product_product(id,product_tmpl_id,barcode,default_code,active) "\
    +" values("+row[0]+","+row[1]+",'"+row[0]+"','"+row[0]+"',True)"\
    +" ON CONFLICT ON CONSTRAINT product_product_pkey DO UPDATE SET active=True,default_code='"+row[0]+"'"+",barcode='"+row[0]+"'"
    cursor.execute(statement)
    conn.commit() 
    statement=""
    statement="INSERT INTO product_attribute_line_product_attribute_value_rel("\
    +"product_attribute_line_id, product_attribute_value_id) VALUES("\
    +row[0]+",1) ON CONFLICT ON CONSTRAINT product_attribute_line_product_a_product_attribute_line_id_fkey DO NOTHING;"
    print statement
    
    #cursor.execute(statement)
    #conn.commit()
    