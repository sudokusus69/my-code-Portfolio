import numpy as np


def define_array():
    
    arr = np.array([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]])
    ar = arr.astype(float)

    print(ar)
    print(ar.dtype)

    for x in np.nditer(arr):
        print(x)

    for x in np.ndenumerate(arr):
        print(x)     

    for x,y in np.ndenumerate(arr):
        print(x,y)


def ndenumerate_array():
    # use the ndenumerate method in 2d array
    expanded_2d = np.array([[1, 2, 3], [4, 5, 6]])
    for x,t in np.ndenumerate(expanded_2d):
        print(x,t)

    # use the ndenumerate method in 3d array
    expanded_3d = np.array([[[1, 11], [2, 22]], [[3, 33], [4, 44]]])
    for x,t in np.ndenumerate(expanded_3d):
        print(x,t)


        
    # use the ndenumerate methos in 4d array
    expanded = np.array([
        [[[1, 10], [2, 20], [3, 30], [4, 40]],
        [[5, 50], [6, 60], [7, 70], [8, 80]],
        [[9, 90], [10, 100], [11, 110], [12, 120]]],
        
        [[[13, 130], [14, 140], [15, 150], [16, 160]],
        [[17, 170], [18, 180], [19, 190], [20, 200]],
        [[21, 210], [22, 220], [23, 230], [24, 240]]]
    ])

    for x,t in np.ndenumerate(expanded):
        print(x,t)    


