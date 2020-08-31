import pandas as pd
import os 
import sys

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
print (script_dir)
cars_file_path = "datasets/cars.csv"
cars_abs_file_path = os.path.join(script_dir, cars_file_path)
cars = pd.read_csv(cars_abs_file_path)

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




