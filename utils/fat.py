from utils import connector
def get_low_fat():
    mydb = connector.connect()
    mycursor = mydb.cursor()
    sql = "SELECT * FROM NUTRITION N,FAT F WHERE N.FID=F.FID ORDER BY F.TOTAL_FAT LIMIT 50"
    mycursor.execute(sql)
    data = mycursor.fetchall()
    return data

def get_food_fat(name):
    mydb = connector.connect()
    mycursor = mydb.cursor()
    sql = "SELECT F.TOTAL_FAT,F.SATURATED_FAT,N.NAME FROM NUTRITION N,FAT F WHERE N.FID=F.FID AND N.NAME LIKE '%{}%'".format(name)
    mycursor.execute(sql)
    data = mycursor.fetchall()
    return data

