import psycopg2
conn = psycopg2.connect("host='192.168.1.36' dbname='odoo' user='postgres' password='odo'")
cursor=conn.cursor()