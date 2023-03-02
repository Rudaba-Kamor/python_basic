def Calculate(a,c,b):
    if(c=="+"):
        Addition(a,b)
    elif(c=="-"):
        Substraction(a,b)    
    elif(c=="*"):
        Multiplication(a,b)
    elif(c=="/"):
        Division(a,b)
    elif(c=="compare"):
        Greaterthan_tester(a,b)
    elif(c=="%"):
        Modulus(a,b)    
    else:
        print("ERROR")                  


def Addition(a,b):
    print(a+b)

def Substraction(a,b):
    print(a-b)

def Multiplication(a,b):
    print(a*b)        

def Division(a,b):
    print(a/b)

def Modulus(a,b):
    print(a%b)

def Greaterthan_tester(a,b):
    if(a>b):
       
        print(a,"greater than",b)
      
       
    elif a==b:
        
        print(a,"equal to",b)
          
    else:
        print(a,"less than",b)
        

