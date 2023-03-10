import numpy as np

array = np.array([12, 24, 35, 41, 55, 67])

newarr = np.array_split(array, 3)

print(newarr)

#Access the splitted arrays:

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr[0])
print(newarr[1])
print(newarr[2])

# Split the 2-D array into three 2-D arrays.
array = np.array([[19, 2], [3, 48], [5, 6], [7, 8], [98, 10], [11, 12]])

newarr = np.array_split(array, 3)

print(newarr)

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.array_split(arr, 3, axis=1)

print(newarr)