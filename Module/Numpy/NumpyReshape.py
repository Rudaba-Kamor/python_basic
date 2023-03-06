import numpy as np

# Check if the returned array is a copy or a view->  returns the original array, so it is a view.

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

print(arr.reshape(2, 4).base)

# Convert 1D array with 8 elements to 3D array with 2x2 elements:

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

newarr = arr.reshape(2, 2, -1)

print(newarr)

# Convert the array into a 1D array:

arr = np.array([[1, 2, 3], [4, 5, 6]])

newarr = arr.reshape(-1)

print(newarr)