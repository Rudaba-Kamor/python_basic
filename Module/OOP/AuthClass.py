class AuthClass:
    profileData = ""
    # name = "Rudaba"
    # password = "12345"
    login = False
    
    def __init__(self):
        print("auth class initiate")

    def LoginMethod(self):
        name = input(" Enter Name: ")
        password = input(" Enter Password: ")

        import mysql.connector
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="campus"
        )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM user WHERE name='"+ name +"' and password='"+ password +"'")
        myresult = mycursor.fetchall()
        # print(myresult)

        if myresult:
            self.login = True
            self.profileData =  myresult
            print("Login Success")
            self.profileMethod()
        else:
            print("Invalid name or password!")
            self.profileMethod()
    
    def isLoggedIn(self):
        if (self.login):
            return True
        else:
            return False

    def profileMethod(self):
        if self.isLoggedIn():
            print("Welcome !")
            print("Your Name:  - This is your profile home")
            print(self.profileData)
        else:
            print("404 Not Found !")
            self.LoginMethod()