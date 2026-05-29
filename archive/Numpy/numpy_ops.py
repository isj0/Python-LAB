import numpy as np

##### Join Numpy Arrays #######

# Join 1D Array
# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
# arr = np.concatenate((arr1, arr2))
# print(arr)

# # Join 2D Arrays
# arr1 = np.array([[1, 2], [3, 4]])
# arr2 = np.array([[5, 6], [7, 8]])
# arr = np.concatenate((arr1, arr2), axis = 1)
# print(arr)
# newarr = np.concatenate((arr1, arr2), axis = 0)
# print(newarr)

## Stacking Arrays
# Join 1D Array
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
# arr = np.stack((arr1, arr2), axis = 1)
# print(arr)
# arr = np.hstack((arr1, arr2))
# print(arr)
# arr = np.vstack((arr1, arr2))
# print(arr)

########### Array Split ##############
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr = np.array_split(arr, 3)
print(newarr)

