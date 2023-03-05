import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr[1])


#  2-D arrays- Access the element on the first row, second column:

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('2nd element on 1st row: ', arr[0, 1])


# 3-D array

arr = np.array(
    [
     [
       [1, 2, 3], [4, 5, 6]
     ],
      [
    [7, 8, 9], [10, 11, 12]
      ]
    ]
    )

print(arr[0, 1, 2])

# NEgative Indexing

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('Last element from 2nd dim: ', arr[1, -1])