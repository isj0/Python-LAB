import numpy as np

########## Searching Arrays ###########

# arr = np.array([1, 2, 3, 4, 5, 4, 4])
# x = np.where(arr == 4)
# print(x)

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# x = np.where(arr%2 == 0)
# print(x)

# find the index where value should be inserted to maintain search order
# arr = np.array([6, 7, 8, 9])
# x = np.searchsorted(arr, 7)
# print(x)

########## Sorting Arrays #############
arr = np.array([3, 2, 0, 1])
# this method returns the copy array sorted keeping the original array unchanged
print(np.sort(arr))

arr = np.array([True, False, True])
print(np.sort(arr))

# Sorting 2D array
arr = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr))
