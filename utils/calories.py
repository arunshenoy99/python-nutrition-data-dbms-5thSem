from utils import connector
def get_calories(data):
    mydb = connector.connect()
    mycursor = mydb.cursor()
    sql = "SELECT * FROM NUTRITION WHERE CALORIES BETWEEN {} AND {}".format(int(data)-2,int(data)+2)
    mycursor.execute(sql)
    dat = mycursor.fetchall()
    return dat
