import psycopg2
import datetime
conn = psycopg2.connect("host='localhost' dbname='odoo' user='postgres' password='odoo'")
cursor=conn.cursor()
cursor.execute("""SELECT * from mclass""")
rows = cursor.fetchall()
for row in rows:
    statement=" Insert into product_category(id,name) "\
    +" values("+str(row[0])+",'"+row[1]+"')" \
    +" ON CONFLICT ON CONSTRAINT product_category_pkey DO UPDATE SET complete_name='"+row[1]+"';"
    cursor.execute(statement)
    conn.commit() 
    



    