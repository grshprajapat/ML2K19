#!/usr/bin/python3
import mysql.connector as mysql
#rds information
u='root'
p='v'
db='adhhoc'
h='endpoint'


#now connecting
conn=mysql.connect(user=u,password=p,database=db,host=h)
#now generating a sql language  cursor
cur=conn.cursor()

#now we can write sql  query

cur.execute("show tables;")


print(cur.fetchall())
#close database connnection
conn.close()

