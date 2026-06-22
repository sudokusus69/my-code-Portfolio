import numpy as np 
from scipy.sparse  import csr_matrix, csc_matrix, coo_matrix

arr1 = np.array(([1, 0, 0, 0, 2, 0, 3, 0, 0, 4], [0, 5, 0, 0, 0, 6, 0, 0, 7, 0]))

print(csr_matrix(arr1).data) #slices the data row wise
print(csc_matrix(arr1).data) #slices the data column wise

# the .data func is used to store the data which is being sliced into i.e 
# the terminal will display the sliced data for ex--- [1 2 3 4 5 6 7]

print(csr_matrix(arr1).count_nonzero()) 
print(csr_matrix(arr1).nnz) #nnz is used to count the number of non zero elements in the sparse matrix
print(csr_matrix(arr1).shape) #shape is used to get the shape of the sparse matrix
print(csr_matrix(arr1).indices) #indices is used to get the indices of the non zero elements in the sparse matrix


elim = csr_matrix(arr1).tocsc() #converts the csr matrix to csc matrix
print(elim.data) # displays the data before eliminating the zeros
elim.eliminate_zeros() #eliminates the zeros from the sparse matrix
print(elim.data) # displays the data after eliminating the zeros

dup = csr_matrix(arr1)
dup.sum_duplicates()
print(dup.data)
# it is used to remov the duplicate entries in the sparse matrix