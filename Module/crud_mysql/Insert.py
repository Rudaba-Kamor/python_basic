import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="campus"
)

name = input("Enter Student name: ")
roll = input("Enter Student roll: ")
studentClass = input("Enter Student class: ")

mycursor = mydb.cursor()

sql = "INSERT INTO student (name, roll,class) VALUES (%s, %s, %s)"
val = (name, roll,studentClass)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")