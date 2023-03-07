import numpy as np

myarr = np.array([11, 22, 33])

for x in myarr:
  print(x)


#####


myarr = np.array([[1, 2, 3], [4, 5, 6]])

''''for x in myarr:
  print(x)'''
for x in np.nditer(myarr):
  print(x)

 ##### 

ar = np.array([[1, 2, 3], [4, 5, 6]])

for x in ar:
  for y in x:
    print(y)