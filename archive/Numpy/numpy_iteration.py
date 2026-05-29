import numpy as np

####### Iterating over Arrays #########

# arr = np.array([1, 2, 3])
# # iterating over 1D array
# for x in arr:
#     print(x)

# arr = np.array([[1, 2, 3], [4, 5, 6]])
# # iterating over 2D array
# for x in arr:
#     for y in x:
#         print(y)

# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# for x in arr:
#     print(x)

# using nditer() function
arr = np.array([[[1, 2], [3, 4], [5, 6], [7, 8]]])

for x in np.nditer(arr):
    print(x)