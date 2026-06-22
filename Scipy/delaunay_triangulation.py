import numpy as np 
from scipy.spatial import Delaunay, ConvexHull, KDTree, distance
import matplotlib.pyplot as plt

arr = np.array([[1,1],[2,2],[1,4],[3,1]])


a = arr[:,0] # it is used to extract the first column of the array
b = arr[:,1] # it is used to extract the second column of the array
plt.triplot(a, b, Delaunay(arr).simplices) 
# it is used to plot the Delaunay triangulation of the points in the array
plt.scatter(a,b, color = 'blue')
plt.show()



    # the convex hull is used to find the smallest polygon
    # that can be formed that covers all the other given points in the graph(array)

hull = ConvexHull(arr).simplices
plt.scatter(arr[:,0], arr[:,1], color = 'blue')
for x in hull:
        plt.plot(arr[x,0], arr[x,1], 'r-')

plt.show()


q = KDTree(arr).query((3,2))
print(q)

