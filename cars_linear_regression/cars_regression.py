import matplotlib.pyplot as plt
import pandas as pd 
import os
import sys

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
print (script_dir)
cars_file_path = "../ingest_analyze/datasets/cars_dataset.csv"
cars_abs_file_path = os.path.join(script_dir, cars_file_path)
cars = pd.read_csv(cars_abs_file_path, skipinitialspace=True)


#lets find a linear regression between mpg and horsepower

#take out the dependent and independent variables
cars = cars.iloc[:,[1,6]]
print (cars.head())

cars.plot(x='price', y='mileage', style='x')
plt.xlabel("price")
plt.ylabel("mileage")

plt.show(block=False)

#prepare data for linear regression
x = pd.DataFrame(cars['price'])
y = pd.DataFrame(cars['mileage'])

X_train, X_test, Y_train, Y_test = train_test_split(x,y, test_size=0.2, random_state = 1 )

print(X_train.shape)
print(X_test.shape)
print(Y_train.shape)
print(Y_test.shape)

regression = LinearRegression()
regression.fit(X_train,Y_train)

print ("regression intercept " + str(regression.intercept_))
print ("regression coef " + str(regression.coef_))

y_pred = regression.predict(X_test)
y_pred = pd.DataFrame(y_pred, columns=['Predicted'])

print (y_pred)

plt.plot(X_test, regression.coef_*X_test + regression.intercept_)

#plt.show()

plt.savefig('cards_linear_reg.png')


