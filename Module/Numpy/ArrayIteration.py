import numpy as np

myarr = np.array([11, 22, 33])

for idx, x in np.ndenumerate(myarr):
  print(idx, x)