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

##Create a new list called 'crimes' and print the contents using a for loop
crimes = ["theft", "rape", "burglary", "robbery", "violent_crime", "murder_ms", "agg_assault", "prop_crimes"]
for item in crimes:
    print(item)

for i in range(len(crimes)):
        element = crimes[i]
        if type(element) == int:
            sequence[i] = element + 4

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

##add all rows to see total crime in each state and add as a column
column_list = list(df)
print(column_list)
column_list.remove("Location")
print(column_list)
df["Total Crime"] = df[column_list].sum(axis=1)
print(df)

##sort by 'Total Crime' to see what location has the most crime overall
print(df.sort_values(by='Total Crime', ascending=False))

##find the mean of the column 'Total Crime' to find out what the average number of crimes are a year per location in the USA.
print(df["Total Crime"].mean())

##find the totals of each crime and print them
violent_crime_sum = df["violent_crime"].sum()
print(violent_crime_sum)
murder_ms_sum = df["murder_ms"].sum()
print(murder_ms_sum)
rape_sum = df["rape"].sum()
print(rape_sum)
robbery_sum = df["robbery"].sum()
print(robbery_sum)
agg_assault_sum = df["agg_assault"].sum()
print(agg_assault_sum)
prop_crimes_sum = df["prop_crimes"].sum()
print(prop_crimes_sum)
burglary_sum = df["burglary"].sum()
print(burglary_sum)
theft_sum = df["theft"].sum()
print(theft_sum)

#make a new list total crimes
total_crimes_sums = [violent_crime_sum, murder_ms_sum, rape_sum, robbery_sum, agg_assault_sum, prop_crimes_sum, burglary_sum, theft_sum]

#show the most common crime
total_crimes_sums.sort()
print('sorted list: ', total_crimes_sums)

#plot a graph of total crime per location
df.plot(x="Location", y="Total Crime")