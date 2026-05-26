import pymysql


def connect_db():
    try:
        connection = pymysql.connect(user = 'root',password = 'root@#RCB',port = 3306,database = 'g1',charset = 'utf8',host = 'localhost')
        print("DB Connect")
        return connection
    except:
        print("DB connection failed")

def dissconnection_db(connection):
    try:
        connection.close()
        print("DB Disconnected")
    except:
        print("DB disconnection failed")

def create_table():
    query = 'CREATE TABLE IF NOT EXIST people (id INT PRIMARY KEY AUTO_INCREMENT,name VARCHAR(64) NOT NULL,gender BOOL NOT NULL,age int default(0),location VARCHAR(32));'
    try:
        connection = connect_db()
        cursor = connection.cursor()
        count = cursor.execute(query)
        if count == 0:
            print("table is created")
        else:
            print("table is not created")
        cursor.close()
        dissconnection_db(connection)
    except:
        print("tbale creation failed")

create_table()