from dbService import createConnection, executeQuery, closeConnection

def getData():
    try : 
        conn = createConnection()
        cursor = conn.cursor()
        query = "select * from data"
        executeQuery(cursor=cursor, query=query)
        data = cursor.fetchall()
        result = []
        for row in data:
            row_dict = {}
            for idx, column in enumerate(cursor.description):
                row_dict[column[0]] = row[idx]
            result.append(row_dict)
        return result 
    except Exception as err:
        print(str(err))

    finally:
        closeConnection(cursor=cursor)

def addData(body):
    try : 
        conn = createConnection()
        cursor = conn.cursor()
        query = f"INSERT INTO `data` VALUES ('{body['id']}','{body['fname']}','{body['lname']}','{body['email']}','{body['gender']}')"
        print(query)
        executeQuery(cursor=cursor, query=query)
    except Exception as err:
        print(str(err))
    finally:
        closeConnection(cursor=cursor)

def changeData(body):
    try : 
        conn = createConnection()
        cursor = conn.cursor()
        query = f"""
            UPDATE `data` 
            SET 
                `first_name` = '{body['fname']}', 
                `last_name` = '{body['lname']}', 
                `email` = '{body['email']}', 
                `gender` = '{body['gender']}'
            WHERE 
                `id` = '{body['id']}'
        """
        print(query)
        executeQuery(cursor=cursor, query=query)
    except Exception as err:
        print(str(err))
    finally:
        closeConnection(cursor=cursor)



def removeData(body) : 
    try : 
        conn = createConnection()
        cursor = conn.cursor()
        # query = f"""
        #     UPDATE `data` 
        #     SET 
        #         `first_name` = '{body['fname']}', 
        #         `last_name` = '{body['lname']}', 
        #         `email` = '{body['email']}', 
        #         `gender` = '{body['gender']}'
        #     WHERE 
        #         `id` = '{body['id']}'
        # """
        # print(query)
        query = f"DELETE FROM data where id = {body['id']}"
        executeQuery(cursor=cursor, query=query)
    except Exception as err:
        print(str(err))
    finally:
        closeConnection(cursor=cursor)