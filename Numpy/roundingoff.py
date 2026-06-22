import numpy as np

# rounding off decimal values in numpy array
a = np.array([1.2, 2.5,5.998,  3.7, 4.9])
print(np.round(a))
print(np.around(a, 1))  # rounding to 1 decimal place
print(np.ceil(a))  # rounding up to the nearest integer
print(np.floor(a))  # rounding down to the nearest integer

import numpy as np
arr = np.trunc([5.998, 1.455])
print(arr)