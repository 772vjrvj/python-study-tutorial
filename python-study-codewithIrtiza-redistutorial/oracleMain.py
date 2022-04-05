import cx_Oracle
import os
import redis
import time
redis_host = 'localhost'
redis_port = 6379

r = redis.StrictRedis(
    host=redis_host, port=redis_port, decode_responses=True)

LOCATION = r"E:\instantclient_21_3"
os.environ["PATH"] = LOCATION + ";" +os.environ["PATH"] #환경변수 등록

connect = cx_Oracle.connect("scott", "tiger", "localhost:1521/orcl")
cursor = connect.cursor()

result_list = []

for name in ['test','test','test','test','test','test','test','test','test','test']:
  name = name
  first_time = time.time()
  result = r.get(name=name)
  print(name)
  print(result)

  if not result:
      print("캐시에서 가져오지 못함")
      sql = '''select name, id from member where name= :name'''
      cursor.execute(sql, name)
      result = cursor.fetchone()
      r.set(name=result[0], value=result[1])


  else:
      print("캐시에서 가져옴!")

  result = r.get(name=name) #if문에 넣을수있지만 동일한 조건을 주기위함
  last_time = time.time()
  timetotime = last_time-first_time
  print(timetotime, "초 걸림")
  print(result)
  result_list.append(timetotime)
    
print("완료")
print(sum(result_list)/len(result_list))