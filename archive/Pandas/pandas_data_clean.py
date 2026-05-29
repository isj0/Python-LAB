import pandas as pd

df = pd.read_csv("data_set.csv")
# print(df.head())

# return dataframe with no empty cells
# by defauly dropna() returns a new dataframe
# new_df = df.dropna()
# print(new_df.to_string())

# # if you want to change the original dataframe, 
# df.dropna(inplace=True)
# print(df.head().to_string())

# replace empty values
# instead to deleting entire rows, use
# fillna() to replace empty cells with a value

# df = pd.read_csv("data_set.csv")
# df.fillna(130, inplace=True)
# print(df.head().to_string())

# df = pd.read_csv("data_set.csv")
# df.fillna({"Calories": 130}, inplace=True)
# print(df.head())

# A common way to replace to empty cells,
# is to calculate mean, median, or mode
print(df.columns)
# x = df["Calories"].mean()
# df.fillna({"Calories": x}, inplace=True)
# print(df.head())