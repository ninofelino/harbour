from sqlalchemy import *

import psycopg2
import datetime
conn = psycopg2.connect("host='localhost' dbname='db' user='postgres' password='odoo'")
cursor=conn.cursor()

listOfUkuran=['O','S','M','L','XL','2','3','4','5','6','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45']


from dbfread import DBF
from sqlalchemy import Table, MetaData, create_engine
from sqlalchemy import text
from sqlalchemy.dialects.postgresql import insert
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
    con = engine.connect() 
    cursor.execute("""SELECT * from invvariant""")
    rows = cursor.fetchall()
    con.execute(text("delete from product_attribute_line"))
    for row in rows:
        print "   ", row[0]
        con.execute(text("Insert into product_attribute_line(id,product_tmpl_id,attribute_id,create_uid,write_uid) VALUES(:id,:product_tmpl_id,:attribute_id,:create_uid,:write_uid)")\
        ,{"id":row[0],"product_tmpl_id":row[0],"attribute_id":1,"create_uid":1,"write_uid":1})\
       
        statement=" Insert into product_template(id,name,sequence,type,categ_id,uom_id,uom_po_id,responsible_id,tracking,sale_delay,active) "\
        +" values("+row[0]+",'"+row[2]+"',0,'consu',1,1,1,1,'no-message',1,True) "\
        +" ON CONFLICT ON CONSTRAINT product_template_pkey DO UPDATE SET tracking='"+"none"+"',active=True,purchase_ok=True,list_price="+str(row[7])+",sale_ok=True,categ_id=mclass('"+row[10]+"');"
        print row[7]
        try :
             cursor.execute(statement)
             conn.commit() 
        except:
             print "error"      
          

def productvariant():
    print "Product Variant"
    con = engine.connect() 
    con.execute(text("delete from product_attribute_line_product_attribute_value_rel"))
   
    cursor.execute("""SELECT * from invproduct_product order by 2,1""")
    rows = cursor.fetchall()
    x=0
    jml=0
   
    for row in rows:   
               con.execute(text("INSERT INTO product_attribute_line_product_attribute_value_rel VALUES (:attribute_line_id, :attribut_value)"),\
               {"attribute_line_id": row[1], "attribut_value": row[5]})
               #.on_conflict_do_nothing()
          
               statement=" Insert into Product_product(id,product_tmpl_id,barcode,default_code,active,create_uid,write_uid) "\
               +" values("+row[0]+","+row[1]+",'"+row[0]+"','"+row[0]+"',True,1,1)"\
               +" ON CONFLICT ON CONSTRAINT product_product_pkey DO UPDATE SET write_date='2018-12-01 07:52:30.281056',create_date='2018-12-01 07:52:30.281056',create_uid=1,write_uid=1,active=True,default_code='"+row[0]+"'"+",barcode='"+row[0]+"'"
               try:
                  cursor.execute(statement)
                  conn.commit()
               except:  
                  print "Error"
                  print row[1]
       
              
        
       
       # try:
       #    
       # except:
           
       #    print "error value rel"
             
            
        
       
         #conn.commit()
        


importodoo()
productvariant()
#depstore()
    
        
#mclass()