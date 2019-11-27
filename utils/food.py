from utils.connector import connect
def get_food(name):
    mydb = connect()
    mycursor = mydb.cursor()
    sql = "SELECT * FROM NUTRITION WHERE NAME LIKE '%{}%'".format(name)
    mycursor.execute(sql)
    data = mycursor.fetchall()
    return data

def put_food(data):
    mydb = connect()
    mycursor = mydb.cursor()
    sql = "INSERT INTO NUTRITION(NAME,SERVING_SIZE,CALORIES) VALUES (%s,%s,%s)"
    val = (data['name'],data['serving_size'],data['calories'])
    mycursor.execute(sql,val)
    mydb.commit()
    return mycursor.lastrowid

