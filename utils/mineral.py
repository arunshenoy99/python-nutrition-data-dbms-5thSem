from utils import connector
def get_minerals(data):
    mydb = connector.connect()
    mycursor = mydb.cursor()
    part_sql = ("{},"*len(data["fields"])).format(*data["fields"])
    sql = "SELECT "+ part_sql[:-1]+ " FROM NUTRITION N,MINERAL M WHERE N.FID=M.FID AND N.NAME=%s"
    val = (data["name"],)
    mycursor.execute(sql,val)
    new_data = mycursor.fetchall()
    return new_data

def get_water():
    mydb = connector.connect()
    mycursor = mydb.cursor()
    sql = "SELECT N.NAME,M.WATER FROM NUTRITION N,MINERAL M WHERE N.FID=M.FID ORDER BY M.WATER DESC LIMIT 50"
    mycursor.execute(sql)
    data = mycursor.fetchall()
    return data