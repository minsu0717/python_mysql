import mysql.connector

from mysql_connection import get_connection

try:
    # 1. db에 연결
    connection = get_connection()
    
    
    id = 6
    
    # 2. 쿼리문 만들고
    query = '''delete from test 
                where id = %s;'''
    # 파이썬에서, 튜플만들때, 데이터가 1개인 경우에는
    # 콤마를 꼭 써준다
    record = (id,)
    # 3. 커넥션으로부터 커서를 가져온다            
    cursor = connection.cursor()
    
    # 4. 쿼리문을 커서에 넣어서 실행한다.
    cursor.execute(query,record)
    
    # 5. 커넥션을 커밋한다.=> 디비에 영구정으로 반영하라는 뜻
    connection.commit()
except mysql.connector.Error as e :
    print('Error',e)
finally :
    if connection.is_connected():
        cursor.close()
        connection.close()
        print('MySQL connection is closed')