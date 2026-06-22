import numpy as np



array_1d = np.arange(12)
# filter with condition
# filter with mask
a = array_1d > 5
numbers = array_1d[a]
print(numbers)
# filter with condition
numbers = array_1d[array_1d > 5]
print(numbers)
