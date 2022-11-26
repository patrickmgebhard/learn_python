import numpy as np

a = np.array([1, 2, 3])
print(a.ndim)
print(a.shape)

b = np.array([[1], [2], [3]])
print(b.ndim)
print(b.shape)

c = np.array([[1, 2], [2, 3], [3, 4]])
print(c.ndim)
print(c.shape)

d = np.ones((5, 3, 3))
print(d)

# check out dot product
f = np.dot([[1, 3], [2, 4]], [2, 4])
print(f)