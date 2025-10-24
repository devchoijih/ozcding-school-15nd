import pymysql
import datetime

# (1) db connection
connection = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='',
    db='testdatabase',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

## 1. SELECT * FROM
def select_all():
    with connection.cursor() as cursor:
        sql = "SELECT * FROM users"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

## 2. INSERT INTO
def add_customer(username, email):
    with connection.cursor() as cursor:
        sql = "INSERT INTO users (username, email) VALUES (%s, %s)"
        cursor.execute(sql, (username, email))
        connection.commit()

##3. UPDATE INFO
def update_customer(id, username, email):
    with connection.cursor() as cursor:
        sql = "UPDATE users SET username=%s, email=%s WHERE user_id=%s"
        cursor.execute(sql, (username, email, id))
        connection.commit()

def delete_customer(id):
    with connection.cursor() as cursor:
        sql = "DELETE FROM users WHERE user_id=%s"
        cursor.execute(sql, (id))
        connection.commit()

delete_customer(1)