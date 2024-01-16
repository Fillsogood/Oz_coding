import mysql.connector
from faker import Faker
import random

#mysql 연결 설정
db_connetion = mysql.connector.connect(
    host='localhost',
    user='root',
    password='0000',
    database='mydatabase'
)
#이걸 가지고 컨드롤할 수 있다.
cursor = db_connetion.cursor()
faker = Faker()

#users 테이블에 데이터 삽입
for _ in range(100):
    username =faker.user_name()
    email =faker.email()
    
    sql = "INSERT INTO users(username,email) VALUES(%s,%s)"
    
    values =(username,email)
    cursor.execute(sql,values)

#user_id 불러오기
cursor.execute("SELECT user_id FROM users")
valid_user_id = [row[0] for row in cursor.fetchall()]

# 100개의 주문 더미 데이터 생성
for _ in range(100):
    user_id = random.choice(valid_user_id)
    product_name = faker.word()
    quantity = random.randint(1,10)
    
    try:
        sql = "INSERT INTO orders(user_id,product_name,quantity)  VALUES(%s,%s,%s)"
        values =(user_id,product_name,quantity)
        cursor.execute(sql,values)
    except:
        print("오류발생")
        pass



db_connetion.commit()
cursor.close()
db_connetion.close()