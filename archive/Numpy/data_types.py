import numpy as np

# arr = np.array([1.1, 2.2, 3.1])
# # newarr = arr.astype('i')
# newarr = arr.astype(int)
# print(newarr)
# print(newarr.dtype)

# arr = np.array([1, 0, 3])
# newarr = arr.astype(bool)
# print(newarr)
# print(newarr.dtype)

# arr = np.array([1, 2, 3, 4, 5])
# x = arr.copy()
# arr[0] = 42
# print(arr)

# arr = np.array([1, 2, 3, 4, 5])
# x = arr.view()
# arr[0] = 42
# print(arr)
# print(x)

# arr = np.array([1, 2, 3, 4, 5])
# x = arr.view()
# x[0] = 31
# print(arr)
# print(x)

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
y = arr.view()
print(x.base)
print(y.base)