import numpy as np
import matplotlib.pyplot as plt

x = [35,25,25,15]


plt.pie(x, labels=['Apple', 'Banana', 'Cherry', 'Dates'],colors = ['r','b','m','hotpink'],
         explode=(0.2, 0, 0, 0), autopct='%1.1f%%', startangle=90, shadow = True)

plt.legend(loc = 'upper left')
plt.show()