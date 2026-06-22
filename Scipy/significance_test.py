import numpy as np 
from scipy.stats import ttest_ind, kstest, describe, skew, kurtosis, normaltest
import matplotlib.pyplot as plt

arr = np.random.normal(size = 100)
arr2  = np.random.normal(size = 100)


'''T TESTING'''
x = ttest_ind(arr,arr2).pvalue
# print(x)

'''KS TEST'''

x2 = describe(arr)
# print(x2)

'''NORMALITY TEST'''

x3 = skew(arr)
x4 = kurtosis(arr)
print(x3)
print(x4)

print(normaltest(arr))