import numpy as np

rng = np.random.default_rng()

print(rng.integers(1,7))
print(rng.integers(low=1,high=7, size=3))
print(rng.integers(low=1,high=7, size=(3,2)))

# will reproduce same numbers 
rng_1 = np.random.default_rng(seed=42)
print(rng.random(3))

print(np.random.uniform(low=-1, high=1, size=3))

array = np.array([1,2,3,4,5])
rng.shuffle(array)
print(array)

fruits = np.array(["apple", "custard apple", "kiwi", "orange"])
fruit = rng.choice(fruits, size=2)
print(fruit)

 