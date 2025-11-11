# Numpy -> numerical python
# numpy under hood is written in C which is faster, 10x faster
# numpy allows us to do vectorised operations
import numpy as np

my_list = [1,2,3,4]

my_list = my_list * 2 # 2 4 6 8 2 4 6 8

print(my_list)

arr = np.array([1,2,3,4])
arr = arr * 2

print(arr) # 2 4 6 8

print(type(arr))