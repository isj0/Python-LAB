import numpy as np

# filter an array using a boolean index list
# a boolean index: list of booleans corresponding to indexes in the array

arr = np.array([41, 42, 43, 44])

# hardcoded boolean list
# x = [True, False, True, False]
# newarr = arr[x]
# print(newarr)

#### Create a filter array with elements > 42
# Create n empty list
filter_arr = []

# go through each element in arr
for element in arr:
    # if the element is higher than, 42, set the value to Truem else False
    if element > 42:
        filter_arr.append(True)
    else:
        filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)

# Create a filter array with even elements from the original
arr = np.array([1, 2, 3, 4, 5, 6, 7])

# Create n empty list
filter_arr = []

for element in arr:
    if element % 2 == 0:
        filter_arr.append(True)
    else:
        filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)

# Create a filter array directly from array
arr = np.array([41, 42, 43, 44])
filter_arr = arr > 42
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)

arr = np.array([1, 2, 3, 4, 5, 6, 7])
filter_arr = arr % 2 ==0
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)

