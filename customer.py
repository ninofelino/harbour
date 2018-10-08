import psycopg2
#conn = psycopg2.connect("host='localhost' dbname='admin' user='postgres' password='novellina'")
conn = psycopg2.connect("host='192.168.1.36' dbname='odoo' user='postgres' password='odo'")

cursor=conn.cursor()
from dbfread import DBF
#table res_partner
for item in DBF('/home/server/Downloads/CUS.DBF',encoding='iso-8859-1'):
    print item['CODE'],item['NAME']
    ID="10"+item['CODE'].replace("A","1").replace("B","2") 
    statement ="INSERT INTO res_partner(id,name,company_id,display_name,lang,active,customer,supplier,employee,type,is_company,partner_share,commercial_partner_id,invoice_warn,picking_warn,sale_warn,purchase_warn) VALUES("\
    +ID+",'name',1,'"+item['NAME'].replace("'","")+"','en_US',True,True,False,False,'contact',False,False,"+ID+",'no-message','no-message','no-message','no-message') "\
    +"ON CONFLICT ON CONSTRAINT res_partner_pkey DO UPDATE SET "\
    +"name='"+item['NAME'].replace("'","")+"'"\
    +",display_name='"+item['NAME'].replace("'","")+"'"\
    +",street='"+item['ADD1'].replace("'","")+"'"\
    +",city='"+item['CITY'].replace("'","")+"'"\
    +",color=133"\
    +",ref='"+item['CODE']+"'"\
    +",barcode='"+item['CODE']+"';"
    cursor.execute(statement)
    conn.commit() 