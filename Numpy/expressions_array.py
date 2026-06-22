import numpy as np

# Create a 1D array with 12 elements
array_1d = np.arange(12)

numbers = array_1d[array_1d %2 == 0]
print(numbers)


