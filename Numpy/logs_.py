import numpy as np

# using logariths in numpy


a = np.log(400)
print(a)

b = np.log10(400)
print(b)

c = np.log2(400)
print(c)

d = np.log1p(400)
print(d)

e = np.logaddexp(400, 500)
print(e)

f = np.logaddexp2(400, 500)
print(f)

g = np.logspace(1, 10, num=5)
print(g)

