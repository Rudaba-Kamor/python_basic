fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)


#Looping Through a String
for x in "banana":
  print(x) 

#The break Statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 
  if x == "banana":
    break   

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x) 


for x in range(6):
  print(x) 

for x in range(2, 30, 3):
  print(x) 

#nested loop
adjt = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adjt:
  for y in fruits:
    print(x, y)   