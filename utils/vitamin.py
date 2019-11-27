from utils import connector
def get_vitamins(data):
    mydb = connector.connect()
    mycursor = mydb.cursor()
    sql_part = ("{},"*len(data["fields"])).format(*data["fields"])
    sql = "SELECT "+sql_part[:-1]+" FROM NUTRITION N,VITAMIN V WHERE N.FID=V.FID AND N.NAME=%s"
    val = (data["name"],)
    mycursor.execute(sql,val)
    data_new = mycursor.fetchall()
    return data_new
