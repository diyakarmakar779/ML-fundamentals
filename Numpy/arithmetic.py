import numpy as np

# scalar arithmetic

array = np.array([1, 2, 3])

print(array + 1)

print(array - 2)

print(array * 2)

print(array / 4)

print(array ** 2)

# vectorised math func

print(np.sqrt(array))
array_1 = np.array([1.01, 2.5, 3.99])
print(np.round(array_1))

radii = np.array([1,2,3])
print(np.pi * radii ** 2)

# element wise arithmetic
array1 = np.array([1,2,3])
array2 = np.array([4,5,6])

print(array1 + array2)
print(array1 - array2)
print(array1 * array2)
print(array1 / array2)
print(array1 ** array2)

# comparison operators
scores = np.array([91, 55, 100, 73, 82, 64])

print(scores == 100) # return boolean array
print(scores > 100)

scores[scores < 60] = 0
print(scores)



