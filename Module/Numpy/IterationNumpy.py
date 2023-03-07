import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
  for y in x:
    for z in y:
      print(z)

# only upto 3D

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
  print(x)  




arr = np.array([110, 210, 310, 410])

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
  print(x)      




  ### Problem
  print("PROBLEM! BELOW!!")
  
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]]) 

for x in np.nditer(arr[:, ::2]):
  print(x)