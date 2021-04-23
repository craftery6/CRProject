import pandas as pd

dataset = pd.read_csv("CrimeUSA.csv")

## print first 5 rows
print(dataset.head())

## print missing values
print(dataset.isnull().sum())

import matplotlib.pyplot as plt

import numpy as np

## define dataframe df

df = pd.read_csv("CrimeUSA.csv")
print(df.head())
print(df.tail())

##show the amount of rows
len(df)

##sort data by 'violent_crime'
df.sort_values(by=['violent_crime'])

##selecting a subset of the data
df['theft']

