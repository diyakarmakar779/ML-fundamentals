import numpy as np

array = np.array('A') # O - Dimensional array

array_1 = np.array(['A', 'B', 'C']) # 1 - Dimensional array

array_2 = np.array([['A', 'B', 'C'],
                   ['A', 'B', 'C'],
                   ['A', 'B', 'C']]) #2 - Dimensional array


array_3 = np.array([[['A', 'B', 'C'],['D', 'E', 'F'],['G', 'H', 'I']],
                    [['J', 'K', 'L'],['M', 'N', 'O'],['P', 'Q', 'R']],
                    [['S', 'T', 'U'],['V', 'W', 'X'],['Y', 'Z', ' ']]]) #2 - Dimensional array


print(array.ndim)
print(array_1.ndim)
print(array_2.ndim)
print(array_3.ndim)

print(array_3.shape) # (3,3,3) -> layers, rows, cols

# Chain indexing
print(array_3[0][0][0]) # A

# numpy indexing faster than chain indexing
print(array_3[0, 0, 0 ])

word = array_3[0,1,0] + array_3[0,1,1] + array_3[0,0,1] + array_3[1, 1, 2]
print(word)


 