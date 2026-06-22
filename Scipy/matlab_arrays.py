import numpy as np
from scipy import io 

arr = np.array([1,1,1,1,1,1])
arr2 = np.array([2,2,2,2,2])

x = io.savemat('file1.mat', {'vec2':arr2})
x2 = io.savemat('file1.mat', {'vec':arr})




i = io.loadmat('file1.mat', squeeze_me = True)

print(i['vec'])

