import pandas as pd

# Series is a like a column in a table
# It is one-dimensional array holding data of any type

# a = [1, 7, 2]
# var = pd.Series(a)
# print(var)

# # Labels- rows - with index number, access specified value
# print(var[1])

# Create label with index argument
# a = [1, 7, 2]
# var = pd.Series(a, index = ["x", "y", "z"])
# print(var)
# print(var["y"])

# Use key,value object like dictionary when creating a Series
# Keys of the dictionary becomes the labels
calories = {"day1": 420, "day2": 380, "day3": 390}
var = pd.Series(calories)
print(var)
myvar = pd.Series(calories, index = ["day1", "day2"])
print(myvar)


