import psycopg2
import datetime
conn = psycopg2.connect("host='localhost' dbname='nuansa' user='postgres' password='felino'")
cursor=conn.cursor()



cursor.execute("""SELECT * from invvariant""")
rows = cursor.fetchall()
for row in rows:     
    #print row[0]
    statement="INSERT INTO product_attribute_line_product_attribute_value_rel("\
    +"product_attribute_line_id, product_attribute_value_id) VALUES("\
    +row[0]+",8);"
    #print statement
    try: 
        cursor.execute(statement)
        conn.commit()
    except psycopg2.DatabaseError as error:
        print(error)
    finally:
         print "retry"
         
   
    