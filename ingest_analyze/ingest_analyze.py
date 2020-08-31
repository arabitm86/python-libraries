import pandas as pd
import os 
import sys

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
print (script_dir)
cars_file_path = "datasets/cars.csv"
cars_abs_file_path = os.path.join(script_dir, cars_file_path)
cars = pd.read_csv(cars_abs_file_path, skipinitialspace=True)

print ("Cars type is a " + str(type(cars)))


#Get the first 5 lines of the data sets
print ("****************")
print(cars.head())
print ("****************")

#Get the first 10 lines of the data sets
print ("****************")
print(cars.head(10))
print ("****************")

#Get the last 5 lines of the data sets
print ("****************")
print(cars.tail())
print ("****************")

#view the number of rows and columns in a CSV
print ("****************")
print(cars.shape)
print ("****************")

#Get the mean value for each of the columns
print ("****************")
print(cars.mean())
print ("****************")

#Get the median value for each of the columns
print ("****************")
print(cars.median())
print ("****************")

#Get the max value for each of the columns, only get numbers
print ("****************")
print(cars.max(numeric_only=True))
print ("****************")

#Get the number of non null counts in each column
print ("****************")
print(cars.count())
print ("****************")

#Gets all stats for a dataframe
print ("****************")
print(cars.describe())
print ("****************")

#Rename a column in dataframe
cars = cars.rename(columns={"mpg":"mpg", "cylinders":"cylinders", "cubinches":"cubinches", "hp":"hp", "weightslb":"weightslb", "time-to-60" : "0-2-60", "year":"year", "brand":"brand"})
print (cars)




