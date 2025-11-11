import numpy as np

# aggergate functions = summarise data and typically return a single value

array = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print(np.sum(array))
print(np.mean(array))
print(np.std(array))
print(np.var(array))
print(np.min(array))
print(np.argmin(array)) # index of minimum value
print(np.argmax(array))

print(np.sum(array, axis=0)) # sum of cols
print(np.sum(array, axis=1)) # sum of rows


