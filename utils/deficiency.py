from utils import connector
def get_remedy(name):
    mydb = connector.connect()
    mycursor = mydb.cursor()
    sql = "SELECT * FROM DEFICIENCY WHERE NAME LIKE '%{}%'".format(name)
    mycursor.execute(sql)
    dat = mycursor.fetchall()
    if dat[0][1]=="PROTEIN":
        sql = "SELECT N.NAME FROM PROTEIN P,NUTRITION N WHERE N.FID=P.FID ORDER BY P.PROTEIN DESC LIMIT 50"
        mycursor.execute(sql)
        dat = mycursor.fetchall()
        return (dat,0)
    else:
        sql = "SELECT N.NAME,V.{} FROM VITAMIN V,NUTRITION N WHERE N.FID=V.FID ORDER BY {} DESC LIMIT 50".format(dat[0][1],dat[0][1])
        mycursor.execute(sql)
        newdat=mycursor.fetchall()
        return (newdat,1,dat[0][1])