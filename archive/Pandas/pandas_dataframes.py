# datasets in Panfdas are multi-dim tables, called DataFrames
# Series is like a column, a DataFrame is the whole table

# A Pandas DataFrame is a 2 dim data structure, like  2D Array
# Like a table with rows and columns

import pandas as pd

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 55]
}

# load data into the DataFrame object
df = pd.DataFrame(data)

print(df)

# refer to the row index - this returns a Series
print(df.loc[0])

# use a list of indexes - this return as DataFrame
print(df.loc[[0, 1]])

# with index argument, you can name your own indexes
df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(df)

# use the named index in loc attribute to return specified rows
# refer to the named index
print(df.loc["day2"])