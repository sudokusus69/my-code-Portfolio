import              numpy as np


arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])


def join_array():
    # Example usage
    arr1 = np.array([[1, 2], [3, 4]])
    arr2 = np.array([[5, 6], [7, 8]])
        
    result = np.concatenate((arr1, arr2), axis = 1)
    print(result)  # Output: [[1 2] [3 4] [5 6] [7 8]]

    # a bigger example
    arr1 = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]], )
    arr2 = np.array([[7, 8], [9, 10], [11, 12]])
    result = np.concatenate((arr1, arr2), )
    print(result)  # Output: [[ 1  2] [ 3  4] [ 5  6] [ 7  8] [ 9 10] [11 12]]

def split_array():
        
    newarr = np.array_split(arr1, 3)
    print(newarr[0])




