import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr.dtype)


# For i, u, f, S and U we can define size as well.

arr = np.array([1, 2, 3, 4], dtype='S')

print(arr)
print(arr.dtype)