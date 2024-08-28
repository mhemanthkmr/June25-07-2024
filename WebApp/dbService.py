import mysql.connector
from rich import print

def createConnection() :
    try:
        db_Conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            database="Student"
        )
        db_Conn.autocommit = True
        return db_Conn
    except Exception as err:
        print(str(err))


def executeQuery(query, cursor):
    try:
        cursor.execute(query)
    except Exception as err:
        print(str(err))



def closeConnection(cursor):
    try:
        cursor.close()
    except Exception as err:
        print(str(err))


