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
print(len(df))

##sort data by 'violent_crime'
df.sort_values(by=['violent_crime'])
print(df)

##selecting a subset of the data
print(df['theft'])

##selecting multiple columns
print(df[['theft','rape']])

##show the details of the first column, 'location'
print(df.loc[0])

##Create a new list called 'crimes' and print the contents
crimes = ["theft", "rape", "burglary", "robbery", "violent_crime", "murder_ms", "agg_assault", "prop_crimes"]
for item in crimes:
    print(item)

##Find the index value of 'robbery' in the list
item2 = "robbery"
index = crimes.index(item2)
print(index)

##slicing a list. Select the first 5 rows of the dataset
print(df[:5])

##select the last row of the list
print(df[-1:])

##selecting a subset of rows and columns within the dataframe 'df' to show the violent crime, murder/ manslaughter stats and rape stats of 3 differeyt locations.
print(df.iloc[1:4, 0:4])

##import the requests package & BeautifulSoup
import requests
from bs4 import BeautifulSoup

##scrape URL from the web

URL = 'https://www.factmonster.com/us/states/state-population-by-rank-2015'
r= requests.get(URL)
html_doc = r.text
soup = BeautifulSoup(html_doc)
print(soup.prettify())
print(soup.title)
print(soup.get_text())
for link in soup.find_all('a'):
    print(link.get('href'))

##grouping data by location and violent crime number
df.groupby(["Location", "violent_crime"])

