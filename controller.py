from DBservice import createconnection, executequery, closeconnection

def getdata():
     try :
         connecttion= createconnection()
         cursor=connecttion.cursor()
         query = "select * from guest"
         executequery(cursor = cursor, query = query)
         data = cursor.fetchall()
         result =[]   
         for row in data :
          row_dict = {}
         for idx,column in enumerate(cursor.description):
            row_dict[column[0]] = row[idx]
         result.append(row_dict)

         return data
     
     except Exception as err:
          print(str(err))

     finally:
         cursor.close()
         
