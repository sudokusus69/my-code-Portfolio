import numpy as np

# Create a 1D array with 12 elements
arr = np.arange(12)
print("Original 1D array:")
print(arr)

arr2 = arr.reshape(3,4)
print("\nReshaped to 2D array (2 rows, 4 columns):")
print(arr2)

arr3 = arr.flatten()
print("\nFlattened back to 1D array:")
print(arr3)

arr4 = arr.reshape(2, 2, 3)
print("\nReshaped to 3D array (2 layers, 2 rows, 3 columns):")  
print(arr4)

# raveled array 
# it is used to flatten the array adn view it as a 1D array
arr5 = arr.ravel()