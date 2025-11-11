import numpy as np

# Broadcasting allows NumPy to perform operations on arrays with different shapes by virtually exepanding dimensions so they match the larger arrays shape

# dimensions have the same size OR one of the dimension is 1

array1 = np.array([[1,2,3,4]])
array2 = np.array([[1], [2], [3], [4]])

print(array1.shape)
print(array2.shape)

# dimension read from right to left

print(array1 * array2)

array3 = np.array([[1,2,3,4,5,6,7,8,9,10]])
array4 = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])

print(array3 * array4)