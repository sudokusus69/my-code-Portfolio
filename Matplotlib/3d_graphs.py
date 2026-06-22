import numpy as np
import matplotlib.pyplot as plt

y_axis = [1,2,3,4,10]
x_axis = [1,2,3,4,5]
z_axis = [1,2,3,4,5]

# to create a 3d plot in the graph 
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x_axis, y_axis, z_axis)
plt.show()