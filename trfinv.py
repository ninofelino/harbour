import psycopg2
import datetime
conn = psycopg2.connect("host='localhost' dbname='nuansa' user='postgres' password='felino'")
cursor=conn.cursor()
datakosong =0
listOfUkuran=['2','3','4','5','6','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45']
from dbfread import DBF
for item in DBF('/mnt/share/ICS/DAT/INV.DBF',encoding='iso-8859-1'):
      
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

      if item['LASTRCV'] is None:
              datakosong=datakosong+1
              tglterima ="NULL"
      else: 
              tglterima ="'"+item['LASTRCV'].strftime("%B %d, %Y")+"'"
              print item['LASTRCV'].strftime("%B %d, %Y")
             
     
      if item['CODE'].strip()=="":
         print "Null"
      else:
         statement =" INSERT INTO inv(barcode,article,ukuran,desc1)" \
         +" values('"+item['CODE']+"','"+item['DESC1'].replace("'","")+"','S','"+item['DESC1'].replace("'","")+"')" \
         +" ON CONFLICT ON CONSTRAINT  inv_pkey DO UPDATE SET DESC1='"+item['DESC1'].replace("'","")+"',mclass='"+item['MCLSCODE']+"',hargajual="+str(item['SELLPRC'])+",modal="+str(item['COSTPRC'])\
         +" ,lqoh="+str(item['LQOH'])\
         +",lastrcv="+tglterima \
         +",firstrcv="+awalterima \
         +",ukuran='"+ukuran+"'"+",article='"+article+"'"      
         cursor.execute(statement)
         conn.commit() 