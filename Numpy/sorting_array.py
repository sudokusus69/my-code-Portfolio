import numpy as np

# sorting an array row-wise and column-wise
# Create a 2D array

arr1 = np.array([[3, 1, 2,4,8], [6, 5, 4, 2, 3]])
print("Original 2D array:")
print(arr1)
arr2 = (f'sorted array row-wise: {np.sort(arr1,axis =1 )}')
print( arr2)
arr3 = (f'sorted array column-wise: {np.sort(arr1,axis =0 )}')
print(arr3)