import pandas as pd 
import os
import sys

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
print (script_dir)
cars_file_path = "datasets/cars.csv"
cars_abs_file_path = os.path.join(script_dir, cars_file_path)
cars = pd.read_csv(cars_abs_file_path, skipinitialspace=True)

#Rename a column in dataframe
cars = cars.rename(columns={"weight":"weightlbs"})
print (cars)
print (cars.columns)

#fill null values with mean in dataframe
cars.weightlbs = cars.weightlbs.fillna(cars.weightlbs.mean())
print (cars.head(19))

#find correlation matrix, higher correlation is an indidcation of stronger relationship
#no correlation can be found between attributes of string data type
print (cars[{'mpg', 'cylinders', 'hp', 'time-to-60'}].corr())

#Change column data type from string to float
cars.mpg = cars.mpg.astype (float)
#print the changes
cars.info(null_counts=True)

"""Manpipulating data sets"""

#print the 4th column only
print(cars.iloc[0:5,4])

#print the 6th row to the end with the 4th column to last colum
print(cars.iloc[6:,4:])

#we can even print based on the column name and not just index --> use loc not iloc
print (cars.loc[:,"mpg":"cubicinches"])

#massive replace of a column's value with another value
cars["brand"] = "US"
print(cars)

#double up the records in a column
f = lambda x: x * 2
cars["cylinders"] = cars["cylinders"].apply(f)
print (cars.head())

#sort values by a column
cars.sort_values(by="mpg")
print(cars.head())

#sort values by a column desending
cars.sort_values(by="mpg", ascending="False")
print(cars.head())

#get data based on filters set
filter1 = cars["mpg"] > 15  #<-- on this line we chain more filters
cars_filtered = cars[filter1]
print(cars_filtered.head())

