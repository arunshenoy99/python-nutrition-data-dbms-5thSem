import mysql.connector
def connect():
    mydb = mysql.connector.connect(host="localhost",user="root",database="dbms")
    return mydb