import numpy as np

'''myarr1 = np.array([10, 23, 34])

arr2 = np.array([46, 52, 68])

arrn = np.concatenate((myarr1, arr2))

print(arrn)'''

# 2D 

arr = np.array([[31, 25], [73, 94]])

arr2 = np.array([[65, 69], [37, 18]])
arr3 = np.array([[670, 81], [78, 49]])

myarr = np.concatenate((arr, arr2, arr3), axis=1)

print(myarr)



arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])
arr3 = np.array([[9, 5], [3, 2]])

arr = np.concatenate((arr1, arr2,arr3), axis=0)

print(arr)


arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])
arr3 = np.array([6, 8, 9])


myarr = np.stack((arr1, arr2,arr3), axis=1)

print(myarr) # axis 0 the outcome is same but concatenated