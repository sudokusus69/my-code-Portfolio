import numpy as np 
from scipy.sparse.csgraph  import dijkstra , connected_components,breadth_first_order,depth_first_order, bellman_ford, floyd_warshall
from scipy.sparse import csr_matrix

arr1 = np.array([[0, 1, 0, 0],
                 [1, 0, 1, 0], 
                 [0, 1, 0, -1],
                 [0, 0, 1, 0]])

# Return predecessors method
x = csr_matrix(arr1)
x2 = dijkstra(x, return_predecessors=True, indices=0) 

# print(x2)  # it is used to find the shortest path in a sparse graph.

# connected components method
# print(connected_components(x))

# Floyd-Warshall algorithm
# print(floyd_warshall(x, return_predecessors=True))

# bellman_ford
# print(bellman_ford(x, return_predecessors=True, ))

# depth_first_order
# print(depth_first_order(x, 0, return_predecessors=True))

# breadth_first_order
# print(breadth_first_order(x, 0, return_predecessors=True))