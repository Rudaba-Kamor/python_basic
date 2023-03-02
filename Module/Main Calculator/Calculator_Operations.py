import Operator
import MessageModule


MessageModule.Message("Casio Calculator")

FirstValue=int(input("Enter 1st value please: "))
SecondValue=int(input("Enter 2nd value please: "))
OperationValue=input("Which operator you want to use?: ")


Operator.Calculate(FirstValue,OperationValue,SecondValue)