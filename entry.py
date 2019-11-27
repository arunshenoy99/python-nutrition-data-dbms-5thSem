import csv
from utils import connector
mydb = connector.connect()
mycursor = mydb.cursor()
with open('nutrition.csv') as f:
    data = [tuple(line) for line in csv.reader(f)]
clr3 = "DELETE FROM FAT"
clr2 = "DELETE FROM VITAMIN"
clr1 = "DELETE FROM NUTRITION"
clr4 = "DELETE FROM PROTEIN"
clr5 = "DELETE FROM MINERAL"
sql1 = "INSERT INTO NUTRITION(FID,NAME,SERVING_SIZE,CALORIES) VALUES(%s,%s,%s,%s)"
sql2 = "INSERT INTO FAT(FID,TOTAL_FAT,SATURATED_FAT) VALUES (%s,%s,%s)"
sql3 = "INSERT INTO VITAMIN(FID,A,A_RAE,B12,B6,C,D,E,K) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
sql4 = "INSERT INTO PROTEIN(FID,PROTEIN) VALUES (%s,%s)"
sql5 = "INSERT INTO MINERAL(FID,SODIUM,CALCIUM,IRON,POTASSIUM,CARB,WATER) VALUES (%s,%s,%s,%s,%s,%s,%s)"
val1 = [tuple([int(dat[0])+1,dat[1],dat[2][:-1],dat[3]])for dat in data[1:]]
val2 = [tuple([int(dat[0])+1,dat[4][:-1],dat[5][:-1]]) for dat in data[1:]]
val3 = [tuple([int(dat[0])+1,dat[15][:-2],dat[16][:-3],dat[22][:-3],dat[23][:-2],dat[24][:-2],dat[25][:-2],dat[26][:-2],dat[28][:-3]]) for dat in data[1:]]
val4 = [tuple([int(dat[0])+1,dat[28][:-3]]) for dat in data[1:]]
val5 = [tuple([int(dat[0])+1,dat[7][:-2],dat[29][:-2],dat[31][:-2],dat[35][:-2],dat[58][:-1],dat[76][:-1]]) for dat in data[1:]]
mycursor.execute(clr1)
mydb.commit()
mycursor.execute(clr2)
mydb.commit()
mycursor.execute(clr3)
mydb.commit()
mycursor.execute(clr4)
mydb.commit()
mycursor.execute(clr5)
mydb.commit()
mycursor.executemany(sql1,val1)
mydb.commit()
mycursor.executemany(sql2,val2)
mydb.commit()
mycursor.executemany(sql3,val3)
mydb.commit()
mycursor.executemany(sql4,val4)
mydb.commit()
mycursor.executemany(sql5,val5)
mydb.commit()