import pandas as pd

# load and read csv files
df = pd.read_csv("data.csv")

# print(df.to_string())
# print(df)

print(df.head())
# print(df.head(10))
print()

print(df.tail())
print()

print(df.info())
