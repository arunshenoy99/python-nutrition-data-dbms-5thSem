from utils import connector
def get_vitamins(data):
    mydb = connector.connect()
    mycursor = mydb.cursor()
    if(data["fields"]=="all"):
        sql = "SELECT N.NAME,V.A,V.A_RAE,V.B12,V.B6,V.C,V.D,V.E,V.K FROM NUTRITION N,VITAMIN V WHERE N.FID=V.FID AND N.NAME LIKE '%{}%'".format(data["name"])
        mycursor.execute(sql)
        data_new = mycursor.fetchall()
        return data_new
    sql_part = ("{},"*len(data["fields"])).format(*data["fields"])
    sql = "SELECT NAME,"+sql_part[:-1]+" FROM NUTRITION N,VITAMIN V WHERE N.FID=V.FID AND N.NAME LIKE '%{}%'".format(data["name"])
    mycursor.execute(sql)
    data_new = mycursor.fetchall()
    return data_new
