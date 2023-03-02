'''#Loop through a list
list3=["car", "table", "glasses", "book"]
for x in list3:
    print(x)

#Loop Through the index number
for i in range(len(list3)):
    print("LOOP through index :"+ list3[i])

# Using while loop
#list3=["car", "table", "glasses", "book"]
j=0
while j< len(list3):
    print(list3[j])
    j=j+1    

#Looping using list comprehension
[print(x) for x in list3] '''