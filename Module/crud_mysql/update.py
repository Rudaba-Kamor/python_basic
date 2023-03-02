import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="campus"
)

mycursor = mydb.cursor()

sql = "UPDATE student SET roll = 'cs2' WHERE id = 2"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")