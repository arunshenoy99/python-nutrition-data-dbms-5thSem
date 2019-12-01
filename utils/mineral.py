from utils import connector
def get_minerals(data):
    mydb = connector.connect()
    mycursor = mydb.cursor()
    if(data["fields"]=="all"):
        sql = "SELECT N.NAME,M.SODIUM,M.CALCIUM,M.IRON,M.POTASSIUM,M.CARB,M.WATER FROM NUTRITION N,MINERAL M WHERE N.FID=M.FID AND N.NAME LIKE '%{}%'".format(data["name"])
        mycursor.execute(sql)
        data_new = mycursor.fetchall()
        return data_new
    sql_part = ("{},"*len(data["fields"])).format(*data["fields"])
    sql = "SELECT NAME,"+sql_part[:-1]+" FROM NUTRITION N,MINERAL M WHERE N.FID=M.FID AND N.NAME LIKE '%{}%'".format(data["name"])
    mycursor.execute(sql)
    data_new = mycursor.fetchall()
    return data_new

def get_water():
    mydb = connector.connect()
    mycursor = mydb.cursor()
    sql = "SELECT N.NAME,M.WATER FROM NUTRITION N,MINERAL M WHERE N.FID=M.FID ORDER BY M.WATER DESC LIMIT 50"
    mycursor.execute(sql)
    data = mycursor.fetchall()
    return data