
import psycopg2
conn = psycopg2.connect("host='192.168.1.36' dbname='odoo' user='postgres' password='odo'")
cursor=conn.cursor()
from dbfread import DBF
#table res_partner
x=0
for item in DBF('/home/server/Downloads/MCLS.DBF',encoding='iso-8859-1'):
    print item['CODE'],item['DESC']
    ID="10"+item['CODE'].replace("A","1").replace("B","2") 
    x=x+1
    statement ="INSERT INTO pos_category(id,name) values("\
    +str(x)+",'"+item['DESC']+"') ON CONFLICT ON CONSTRAINT pos_category_pkey DO NOTHING;"
    cursor.execute(statement)
    conn.commit() 