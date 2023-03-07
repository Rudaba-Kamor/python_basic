import numpy as np
from numpy import random

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr3 = np.array([75, 89, 23])

arr4 = np.array([26, 89, 34])

arr = np.concatenate((arr1, arr2, arr3,arr4))
random.shuffle(arr)

print(arr)

for x in arr:
	print ("Products id: ", x)