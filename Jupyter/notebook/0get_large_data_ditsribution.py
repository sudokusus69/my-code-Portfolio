import numpy as np
import matplotlib.pyplot as plt


'UNIFROM DATA DISTRIBUTION'
arr = np.random.uniform(10,2,100)

# plt.hist(arr, 50)
# plt.show()

'''GUASSION DATA DISTRIBUTION / THE BELL CURVE''' 
arr2 = np.random.normal(5, 1,100)

plt.scatter(arr2, arr)
