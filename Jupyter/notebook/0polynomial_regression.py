import matplotlib.pyplot as plt
from scipy import stats
import numpy as np


x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
y = [100,90,100,90,60,60,50,40,50,80,90,100,110,90,90,90,100,120,120,120]


plt.scatter(x,y)

x = np.poly1d(np.polyfit(x,y,3))
y = np.linspace(1,22,100)

plt.plot(y, x(y))
plt.show()



