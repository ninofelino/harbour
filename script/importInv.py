from sqlalchemy import *

import psycopg2
import datetime
conn = psycopg2.connect("host='localhost' dbname='db' user='postgres' password='odoo'")
cursor=conn.cursor()

listOfUkuran=['O','S','M','L','XL','2','3','4','5','6','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45']


from dbfread import DBF
from sqlalchemy import Table, MetaData, create_engine
from sqlalchemy import text

engine = create_engine("postgresql://postgres:odoo@localhost/db")

def mclass():
    cursor.execute("""SELECT * from mclass""") 
    rows = cursor.fetchall()
    for row in rows:
        statement=" Insert into product_category(id,name) "\
        +" values("+str(row[0])+",'"+row[1]+"')" \
        +" ON CONFLICT ON CONSTRAINT product_category_pkey DO UPDATE SET complete_name='"+row[1]+"';"
        cursor.execute(statement)
        conn.commit() 

def depstore():
  datakosong =0
  for item in DBF('/mnt/poserver/ics/DAT/INV018.DBF',encoding='iso-8859-1'):
      list=item['DESC1'].split(" ")
      print list[len(list)-1]
      ukuran=list[len(list)-1][-2:]
      if ukuran in listOfUkuran :
         print ukuran    
         article=item['DESC1'].replace(ukuran,"").replace("'","")
      else:
         ukuran=""     
         print "AllSize"         
         article=item['DESC1'].replace("'","")
         tglterima = datetime.datetime.now()
         awalterima ="NULL"
      if item['FIRSTRCV'] is None:
         awalterima ="NULL"
      else:
         awalterima="'"+item['FIRSTRCV'].strftime("%B %d, %Y")+"'"        

      if item['LQOH'] is None:
         LQOH =0
      else:
         LQOH=item['LQOH']        
 
      if item['LASTRCV'] is None:
         datakosong=datakosong+1
         tglterima ="NULL"
      else: 
         tglterima ="'"+item['LASTRCV'].strftime("%B %d, %Y")+"'"
         print item['LASTRCV'].strftime("%B %d, %Y")
            
      if item['CODE'].strip()=="":
         print "Null"
      else:
         statement =" INSERT INTO inv(barcode,article,ukuran,desc1,mclass,hargajual,modal,lqoh,lastrcv,firstrcv)" \
         +" values('"+item['CODE'][:8]+"','"+article.replace("'","")+"','"+ukuran+"','"+item['DESC1'].replace("'","")+"','"+item['MCLSCODE']+"',"+str(item['SELLPRC'])+","+str(item['COSTPRC'])+","+str(LQOH)+","+tglterima+","+awalterima+")" \
         +" ON CONFLICT ON CONSTRAINT  inv_pkey DO UPDATE SET DESC1='"+item['DESC1'].replace("'","")+"',mclass='"+item['MCLSCODE']+"',hargajual="+str(item['SELLPRC'])+",modal="+str(item['COSTPRC'])\
         +" ,lqoh="+str(LQOH)\
         +",lastrcv="+tglterima \
         +",firstrcv="+awalterima \
         +",ukuran='"+ukuran+"'"+",article='"+article+"'"  
         print article    
         cursor.execute(statement)
         conn.commit()          
        
def importodoo():
    cursor.execute("""SELECT * from invvariant""")
    rows = cursor.fetchall()
    for row in rows:
        print "   ", row[0]
        statement=" Insert into product_template(id,name,sequence,type,categ_id,uom_id,uom_po_id,responsible_id,tracking,sale_delay,active) "\
        +" values("+row[0]+",'"+row[2]+"',0,'consu',1,1,1,1,'no-message',1,True) "\
        +" ON CONFLICT ON CONSTRAINT product_template_pkey DO UPDATE SET tracking='"+"none"+"',active=True,purchase_ok=True,list_price="+str(row[7])+",sale_ok=True,categ_id=mclass('"+row[10]+"');"
        print row[7]
        cursor.execute(statement)
        conn.commit() 
        statement=" Insert into product_attribute_line(id,product_tmpl_id,attribute_id)"\
        +" values("+row[0]+","+row[0]+",1)"
        cursor.execute(statement)
        conn.commit() 

def productvariant():
    print "Product Variant"
    cursor.execute("""SELECT * from invproduct_product order by 2,1""")
    rows = cursor.fetchall()
    x=0
    jml=0
    for row in rows:     
        #print row[0]
        statement=" Insert into Product_product(id,product_tmpl_id,barcode,default_code,active) "\
        +" values("+row[0]+","+row[1]+",'"+row[0]+"','"+row[0]+"',True)"\
        +" ON CONFLICT ON CONSTRAINT product_product_pkey DO UPDATE SET active=True,default_code='"+row[0]+"'"+",barcode='"+row[0]+"'"
        x=x+1
        if x>5 : 
           x=1 
        try:    
           cursor.execute(statement)
           conn.commit() 
        except:
               print "err product"
              
        statement="INSERT INTO product_attribute_line_product_attribute_value_rel("\
        +"product_attribute_line_id, product_attribute_value_id) VALUES("\
        +row[1]+","+str(x)+")"
        # +" ON CONFLICT ON CONSTRAINT product_attribute_line_product_a_product_attribute_line_id_fkey DO NOTHING;"
        #cursor.execute(statement)
        #conn.commit()
        con = engine.connect() 
        try:
            con.execute(text("INSERT INTO product_attribute_line_product_attribute_value_rel VALUES (:attribute_line_id, :attribut_value)"),
               {"attribute_line_id": row[0], "attribut_value": x}) 
        except:
            jml = jml +1
            print "error"
            print jml    
          


#importodoo()
productvariant()
#depstore()
    
        
#mclass()