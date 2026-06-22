from scipy.interpolate import interp1d, UnivariateSpline, Rbf
import numpy as np


'''INTERPOLATION FUNCTION'''
xs = np.arange(10)
xy = xs

inter = interp1d(xs,xy)
inter2 = inter(np.arange(2.1,3,0.1))
print(inter2)


'''SPLINE INTERPOLATION'''

xs = np.arange(10)
xy = xs ** 2 + np.sin(xs)

inter = UnivariateSpline(xs, xy)
inter2 = inter(np.arange(2.1,3,0.1))
print(inter2)



'''RADIAL BASIS FUNCTION'''

xs = np.arange(10)
xy = xs ** 2 + np.sin(xs)

inter = Rbf(xs, xy)
inter2 = inter(np.arange(2.1,3,0.1))
print(inter2)
