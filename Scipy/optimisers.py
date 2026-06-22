import numpy as np
from scipy.optimize import minimize
from math import cos 

def a(x):
    return x**2 +x - 4

myroot = minimize(a,0, method='BFGS')
print(myroot)

myroot2 = minimize(a,0,method='TNC')
print(myroot2)