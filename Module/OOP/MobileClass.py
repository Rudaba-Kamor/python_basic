class MobileClass:
  '''company = ""
  model = ""
  price = ""

  def __init__(self,company,model,price):
    self.company=company
    self.model=model
    self.price=price
    print("Welcome! ")'''

  def Imp_Data(self,company,model,price):
    try:
        import mysql.connector

        mydb = mysql.connector.connect(
          host="localhost",
          user="root",
          password="",
          database="campus"
        )

        mycursor = mydb.cursor()

        sql = "INSERT INTO mobile (company,model, price) VALUES (%s, %s,%s)"
        val = (company,model,price)
        mycursor.execute(sql, val)

        mydb.commit()

        print(mycursor.rowcount, "record inserted.")
    except:
        print("Problem!")

    finally:
        print("Insert again: ")    
        self.insert_values()

  def insert_values(self):
    self.company = input("What is the company?: ")
    self.model = input("What the model?: ")
    self.price = input("Whats the price?: ")
    self. Imp_Data(self.company,self.model,self.price)
