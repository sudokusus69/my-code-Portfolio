import numpy as np 
import matplotlib.pyplot as plt 


# to plot data in bar chart 
x = np.array(['ronaldo', 'messi', 'lamine yamal', 'ronaldinho'])
y = np.array([3,2,20,7])


plt.bar(x, y, color = 'cadetblue', width = 0.2, label= 'bar', alpha = 1)
# plt.barh(x, y, color ='black', height=0.5, label='bar', alpha=1)

plt.legend(loc = 'upper left')
plt.show()