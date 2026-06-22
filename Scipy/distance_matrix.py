import numpy as np 
from scipy.spatial.distance import euclidean, cityblock, cosine, dice, hamming
import matplotlib.pyplot as plt


# euclidean distance

arr1 = np.array([4,50])
arr2 = np.array([2,2])
x = (1,2,3,4, 0)
y = (3,4,3,5, False)

res1 = euclidean(arr1,arr2) 
res2 = cityblock(arr1,arr2)
res3 = cosine(arr1,arr2)
res4 = hamming(x,y)

print(res1)
print(res2) 
print(res3)
print(res4)