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

connecttion= createconnection()
cursor=connecttion.cursor()
query = "select * from room"
cursor.execute(query)
data = cursor.fetchall()

print(data)


db_conn = mysql.connector.connect(
        host ="localhost",
        username = "root",
        password ="Subbu@78",
        database = "HOTEL_MANAGEMENT")

cursor = db_conn.cursor()
query = "select * from guest"
cursor.execute(query)
data = cursor.fetchone()
data = cursor.fetchall()

#print(data)
result = []
for row in data :
    row_dict = {}
    for idx,column in enumerate(cursor.description):
        row_dict[column[0]] = row[idx]
    result.append(row_dict)
print(result)
cursor.close()
