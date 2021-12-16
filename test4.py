import mysql.connector
from mysql.connector.errors import Error

# 연결하는 코드
# try 라고 나오면, 들여쓰기 되어있는 문장들을 싱행하라는 뜻.

try :
    connection = mysql.connector.connect(host='yhdb.ckrtxnsyzas7.ap-northeast-2.rds.amazonaws.com',
        database = 'streamlit_db',
        user = 'python_user',
        password = '1234')    

    query = '''select * 
                from test
                where id = %s;'''
    
    param = (3,)
    
    cursor = connection.cursor()
    
    cursor.execute(query,param)
    
    # select 문은 아래 내용이 필요하다.
    record_list = cursor.fetchall()
    print(record_list)
    
    for row in record_list :
        print('id =',row[0])
        print('name =',row[1])
        print('date =', row[2].isoformat())
# 위의 코드를 실행하다가, 문제가 생기면, except를 실행하라는 뜻.
except Error as e  : 
    print('Error while connecting to MySQL',e)
# finally 는 try에서 에러가 나든 안나든, 무조건 실행하라는 뜻.    
finally :
    cursor.close()
    if connection.is_connected():
        connection.close()
        print('MySQL connection is closed')
    else:
        print('connection does not exist')