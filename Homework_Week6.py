from typing import List

import pandas as pd

# use read_csv to read csv file
f = pd.read_csv('insurance.csv', header=0, sep=',')

df = pd.DataFrame(f)
# read file and store in an array

# Question 2 : print(df.to_string())
print(df.columns)  # indicates the headers representing the columns
print(df.index)  # gives information about the starting and end indices, and the steps of increment
print(df.dtypes)  # gives the types of each column variables
print(df.shape)  # tuple of row and columns (R,C)
print(df.info())  # gives relevant information about the data in the dataframe
print(df.describe())
print(df.corr())

# Question 3 Print age column only
print(df['age'])  # Method 1 : Using [] - Not efficient

# Method 2 : Transpose DataFrame and Use loc or iloc attributes
#transdf = df.T
#print(transdf.loc['age'])
#print(transdf.iloc[0])

# Question 4
# Mathod 1
items1 = ['age', 'children', 'charges']
#print(transdf.loc[items])

# Method 2
subMatrix1 = df[items1]
print(subMatrix1)

# Question 5
subMatrix2 = subMatrix1[0:5]
print(subMatrix2)

# Question 6, 7, 8, 9

selectCharges = df['charges']
print("Mean, Min and Max charges", selectCharges.mean(), selectCharges.min(), selectCharges.max())
# print(df.describe()) # cross-check

##Method 2
val = 10797.3362
nrows = df.shape[0] # how many rows?
for i in range(1, nrows):
    if df.iloc[i]['charges'] == val:
        print("age and sex", df.iloc[i]['age'], " ", df.iloc[i]['sex'])
        print("Smoker?", df.iloc[i]['smoker'])

    if df.iloc[i]['charges'] == df['charges'].max():
        print("Age of person who paid maximum charges", df['charges'].max())

# Method 2
# create a boolean series based on criteria charges =  10797.3362

newCond = df['charges'] == val

print(df[newCond][['age','sex']])
#Question 10, 11 and 12
print('insured children',df['children'].sum())

print(df['region'].value_counts()) # prints the number of occurrences in a column

print(df.corr())