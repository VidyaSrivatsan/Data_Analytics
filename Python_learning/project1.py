import numpy as np
a=np.array([5,6,9])
# print(a[1])

# a=np.array([[1,2], [3,4], [5,6]])
# print(a.ndim)
# print(a.dtype)
# print(a.itemsize)

# a=np.array([[1,2], [3,4], [5,6]], dtype=np.float64)
# print(a.itemsize)
# print(a.shape)

# print(np.arange(1,5))

# print(np.arange(1,5, 2))
# print(np.linspace(1,5, 10))
# print(np.linspace(1,5, 5))

# a=np.array([[1,2], [3,4], [5,6]])
# print(a.reshape(2,3))
# print(a.reshape(6,1))
# print(a.ravel())
# print(a)
# print(a.sum())

# print(a.sum(axis=0))
# print(a.sum(axis=1))
# print(np.std(a))
# print(np.sqrt(a))

# a=np.array([[1,2], [3,4]])
# b=np.array([[5,6], [7,8]])
# print(a)
# print(b)
# print(a+b)
# print(a*b)
# print(a/b)
# print(a.dot(b))
a=np.array([5,6,9])
print(a[0:2])
print(a[-1])
a = np.arange(12) .reshape(3,4)
print(a)
b = a > 4
print(a[b])