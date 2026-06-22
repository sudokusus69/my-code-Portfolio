import numpy as np

arr = np.array([1, 2, 3, 4, 5])

arr2 = []

for x in arr:
    if x >3:
        arr2.append(True)
    else:
        arr2.append(False)
newarr = arr[arr2]



print(arr2)
print(newarr)
