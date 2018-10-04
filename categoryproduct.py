import psycopg2
conn = psycopg2.connect("host='localhost' dbname='odoo' user='postgres' password='novellina'")
cursor=conn.cursor()
from dbfread import DBF
#table res_partner
x=0
for item in DBF('/home/server/Downloads/MCLS.DBF',encoding='iso-8859-1'):
    print item['CODE'],item['DESC']
    ID="10"+item['CODE'].replace("A","1").replace("B","2") 
    x=x+1
    statement ="INSERT INTO product_category(id,name) values("\
    +str(x)+",'"+item['DESC']+"') ON CONFLICT ON CONSTRAINT product_category_pkey DO UPDATE "\
    +" SET name='"+item['DESC']+"'"\
    +" ,complete_name='"+item['DESC']+"';"
    cursor.execute(statement)
    conn.commit() 