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

print (cars[{'mpg', 'cylinders', 'hp', 'time-to-60'}].corr())