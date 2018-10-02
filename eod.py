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
      print item['CODE'],item['DESC1']
     # print item['DESC1']
    