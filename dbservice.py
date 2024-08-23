import mysql.connector 

from rich  import print

def createconnection():
    try:
        db_conn = mysql.connector.connect(
        host ="localhost",
        username = "root",
        password ="Subbu@78",
        database = "HOTEL_MANAGEMENT")

        
        return db_conn

    except Exception as err:
            print(str(err))


def executequery(query,cursor):
    try:
        cursor.execute(query)
    except Exception as err:
        print(str(err))


def closeconnection(cursor):
    try:
        cursor.close()
    except Exception as err:
        print(str(err))





