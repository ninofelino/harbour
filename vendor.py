import psycopg2
conn = psycopg2.connect("host='localhost' dbname='odoo' user='postgres' password='novellina'")
cursor=conn.cursor()
from dbfread import DBF
#table res_partner
for item in DBF('/home/server/Downloads/SUP.DBF',encoding='iso-8859-1'):
    print item['CODE'],item['DESC']
    statement ="INSERT INTO res_partner(id,name,company_id,display_name,lang,active,customer,supplier,employee,type,is_company,partner_share,commercial_partner_id,invoice_warn,picking_warn,sale_warn,purchase_warn) VALUES("\
    +item['CODE']+",'name',1,'display_name','en_US',True,False,True,False,'contact',False,False,"+item['CODE']+",'no-message','no-message','no-message','no-message') "\
    +"ON CONFLICT ON CONSTRAINT res_partner_pkey DO UPDATE SET "\
    +"name='"+item['DESC'].replace("'","")+"'"\
    +",display_name='"+item['DESC'].replace("'","")+"'"\
    +",street='"+item['ADD1'].replace("'","")+"'"\
    +",city='"+item['CITY'].replace("'","")+"'"\
    +",phone='"+item['TELP'].replace("'","")+"'"\
    
      
    cursor.execute(statement)
    conn.commit() 