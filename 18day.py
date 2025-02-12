#PANDAS

import pandas as pd
data = {
    "Name" : ['Ram' , 'Sita' , 'Hari', "Rita", "Ranjana"],
    "Age" : [24, 32, 22, 28, 27] , 
    "City" : ["Kathmandu" , "Pokhara", "Butwal","Lalitpur","Bhaktapur"]
}
df = pd.DataFrame(data)
# print(df)
print(df.describe())


#Reading csv file

import pandas as pd
df = pd.read_csv('new.csv')
print(df)


#Reading SQL file

import pandas as pd
import sqlite3
conn = sqlite3.connect('mydatabase.db')
df = pd.read_sql('SELECT * FROM users', conn)
print(df)


#Data Manipulation

import pandas as pd
data = {
    "Name" : ['Ram' , 'Sita' , 'Hari', "Rita", "Ranjana"],
    "Age" : [24, 32, 22, 28, 27] , 
    "City" : ["Kathmandu" , "Pokhara", "Butwal","Lalitpur","Bhaktapur"]
}

df = pd.DataFrame(data)

# Selecting multiple columns
print(df[['Name', 'Age']])

# Filtering Data
print(df[df["Age"] > 30])

# Adding new Column
df['isAdult'] = df['Age'] > 30
print(df)

# Removing a Column
df.drop(columns = ['Age'], inplace = True)
print(a)
print(df)
df.drop(columns = ['Name'], inplace = True)

# Sorting Data
print(df.sort_values(by='Age' , ascending = False))

# Grouping and Aggregating Data
print(df.groupby("City").mean())


