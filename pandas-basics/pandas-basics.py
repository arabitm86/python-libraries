import pandas as pd

"""series objects are created from one dimensional data"""
data = [1,2,3,4]
series1 = pd.Series(data)
print(series1)
"""
output:
0    1
1    2
2    3
3    4
"""

#checking the type of a series:
print(type(series1))

"""output: <class 'pandas.core.series.Series'>"""

#changing the index names from numbers to letter for example

series_letters = pd.Series(data,index=['a','b','c','d'])
print (series_letters)

"""
Data Frames have:
* columns of different data types
* mutable in size
* labeled axes
* allows arithmetic operations on rows and columns

"""
#creating a dataframe using a list
data_frame = pd.DataFrame(data)
print (data_frame)
"""
   0
0  1
1  2
2  3
3  4
"""

#creating a dataframe using a dictionary
dictionary = {'fruit':['apples', 'banana', 'mangos'], 'count': [10,20,15]}
data_frame = pd.DataFrame(dictionary)
print(data_frame)

"""
    fruit  count
0  apples     10
1  banana     20
2  mangos     15
"""

#creating DataFrame using a series
data = [1,2,3,4]
series2 = pd.Series(data,index=['a','b','c','d'])
data_frame=pd.DataFrame(series2)
print(data_frame)
