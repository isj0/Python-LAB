import numpy as np

# Numpy is used to work with arrays
# The array object is Numpy is called ndarray

# print(np.__version__)

a = np.array(42)

# # use a list and pass to array method, to be converted to nd array object
b = np.array([1, 2, 3, 4, 5])       # 1D Array
# print(arr)
# print(type(arr))

# # use tuple to be converted to ndarray
# arr = np.array((6, 7, 8, 9))
# print(arr)
# print(type(arr))

# This is an example of 2D Array - Matrices
c = np.array([[1, 2, 3], [4, 5, 6]])
# print(arr)

# 3D Arrays - it has 2D Arrays(matrices )  as its elements
# Also known as 3rd order tensor
d = np.array([[[1, 2, 3], [4, 5, 6], ['a', 'b', 'c'], ['d', 'e', 'f']]])
# print(arr)

# ndim attribure return the dimensions of the array
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)