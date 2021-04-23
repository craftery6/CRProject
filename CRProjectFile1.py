import pandas as pd

dataset = pd.read_csv("CrimeUSA.csv")

## print first 5 rows
print(dataset.head())

## print missing values
print(dataset.isnull().sum())
