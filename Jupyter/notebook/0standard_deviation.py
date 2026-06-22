import numpy as np

arr = np.array([20,30,40,50,60,70,80])

'''STANDARD DEVIATION -- σ'''
arr2 = np.std(arr)
print(arr2)

'''VARIATION -- σ2'''
# For each difference: find the square value:
# The variance is the average number of these squared differences:
arr3 = np.var(arr)
print(arr3)

'''PERCENTILE'''
arr4 = np.percentile(arr, 50)
print(arr4)