import numpy as np

a = np.array([1,2,3,4,5])
b = np.array([1,2,3,4,5])


print(np.add(a,b))  # element-wise addition/ sum along columns
print(np.sum(a))  # sum of all elements in a array
print(np.sum([a, b], axis=1)) # sum along rows
print(np.sum([a, b], axis=0)) # sum along columns