import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sample"
)
mycursor = mydb.cursor()
mycursor.executemany( "SELECT* FROM friends")

mydb.commit()
print(mycursor.rowcount,"record inserted.")  

