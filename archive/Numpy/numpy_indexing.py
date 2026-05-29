import numpy as np

b = np.array([1, 2, 3, 4, 5])       # 1D Array
print(b[0])

print(b[2] + b[3])

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print("2nd element of 1st row:", arr[0, 1])
print("5th element of the 2nd row:", arr[1, 4])

d = np.array([[[1, 2, 3], [4, 5, 6], ['a', 'b', 'c'], ['d', 'e', 'f']]])
print("3rd element of the second array:", d[0, 1, 2])

# Negative indexing
print("Last element from 2nd dim:", arr[1, -1])
