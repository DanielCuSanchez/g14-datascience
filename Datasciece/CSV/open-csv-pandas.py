import pandas as pd

file = pd.read_csv("example.csv")

print(file.columns)
print(file.head())
print(file.tail())