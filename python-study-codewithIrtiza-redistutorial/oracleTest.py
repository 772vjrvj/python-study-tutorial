import cx_Oracle
import os
import redis
redis_host = 'localhost'
redis_port = 6379

LOCATION = r"E:\instantclient_21_3"
os.environ["PATH"] = LOCATION + ";" +os.environ["PATH"] #환경변수 등록

connect = cx_Oracle.connect("scott", "tiger", "localhost:1521/orcl")
cursor = connect.cursor()



# SQL
cursor.execute("select title from board")

for i in cursor:
  print(i)
