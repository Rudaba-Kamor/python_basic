# copy is a new array, and the view is just a view of the original array.
import numpy as np
  
# COPY - The copy SHOULD NOT be affected by the changes made to the original array.

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)


# VIEW - The original array SHOULD be affected by the changes made to the view.


arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42

print(arr)
print(x)

# copies owns the data, and views does not own the data

arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

print(x.base)
print(y.base)