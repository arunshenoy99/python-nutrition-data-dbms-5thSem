from utils.connector import connect
mydb=connect()
mycursor = mydb.cursor()
mycursor.callproc('GET_LOG')
for result in mycursor.stored_results():
    print(result.fetchall())