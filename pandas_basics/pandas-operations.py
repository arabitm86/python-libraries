import pandas as pd


player = ['player1', 'player2', 'player3']
points = [ '1', '2', '3']

title = ['Game1', 'Game2', 'Game3']
df1 = pd.DataFrame({'players': player, 'points':points,'title':title})

print("****************")
print(df1)
print("****************")

"""
Output:
   players points  title
0  player1      1  Game1
1  player2      2  Game2
2  player3      3  Game3
"""
player = ['player1', 'player4', 'player5']
kick = [ '1', '4', '5']
punch = [ '1', '4', '5']

df2 = pd.DataFrame({'players': player, 'kicks':kick,'punch':punch})

# perform an inner MERGE on player, result is row with common value of playe across
# sets and adds the new attributes
#By default, a merge is an inner merge
print("****************")
print (df1.merge(df2, on ='players', how='inner'))
print("****************")

"""
 players points  title kicks punch
0  player1      1  Game1     1     1
"""

# perform an INNER LEFT MERGE on player, result is ALL ROWS 
# from LEFT tables will be merged together with value from other DF, 
# values that dont exist = NaN

print("****************")
print (df1.merge(df2, on ='players', how='left'))
print("****************")

"""
Output:
players points  title kicks punch
0  player1      1  Game1     1     1
1  player2      2  Game2   NaN   NaN
2  player3      3  Game3   NaN   NaN
"""

# perform an INNER RIGHT MERGE on player, result is ALL ROWS 
# from RIGHT tables will be merged together, values that dont exist = NaN

print("****************")
print (df1.merge(df2, on ='players', how='right'))
print("****************")

"""
players points  title kicks punch
0  player1      1  Game1     1     1
1  player4    NaN    NaN     4     4
2  player5    NaN    NaN     5     5

"""

# perform an OUTTER MERGE on player, result is ALL ROWS 
# from BOTH tables will be merged together, values that dont exist = NaN

print("****************")
print (df1.merge(df2, on ='players', how='outer'))
print("****************")

"""
  players points  title kicks punch
0  player1      1  Game1     1     1
1  player2      2  Game2   NaN   NaN
2  player3      3  Game3   NaN   NaN
3  player4    NaN    NaN     4     4
4  player5    NaN    NaN     5     5
"""

# With merges it is a MUST to have a common field between both datasets, Joins do
# not need that, and their operations are done on the index, they are made for 
# datasetst that truly dont have anything in common
df1 = pd.DataFrame({'players': player, 'points':points,'title':title}, index=['L1', 'L2', 'L3'])
df2 = pd.DataFrame({'player': player, 'kicks':kick,'punch':punch}, index=['L3','L4', 'L5'])
print("****************")
print (df1.join(df2, how="inner"))
print("****************")
"""
   players points  title   player kicks punch
L3  player5      3  Game3  player1     1     1
"""

#LEFT INNER JOIN: also on common index, and values from left DF are added in with NaN attributes
# from the second DF

print("****************")
print (df1.join(df2, how="left"))
print("****************")
"""
    players points  title   player kicks punch
L1  player1      1  Game1      NaN   NaN   NaN
L2  player4      2  Game2      NaN   NaN   NaN
L3  player5      3  Game3  player1     1     1
"""

print("****************")
print (df1.join(df2, how="right"))
print("****************")
"""
    players points  title   player kicks punch
L3  player5      3  Game3  player1     1     1
L4      NaN    NaN    NaN  player4     4     4
L5      NaN    NaN    NaN  player5     5     5
"""
# OUTER Join does both Left and Right Joints together

print("****************")
print (df1.join(df2, how="outer"))
print("****************")
"""
    players points  title   player kicks punch
L1  player1      1  Game1      NaN   NaN   NaN
L2  player4      2  Game2      NaN   NaN   NaN
L3  player5      3  Game3  player1     1     1
L4      NaN    NaN    NaN  player4     4     4
L5      NaN    NaN    NaN  player5     5     5
"""

# CONCAT Two DataFrames together, this is diff than outer merge, mainly cause 
# the merge is on common attribute, this is on common index, and in this case
# getting all indices
conc = pd.concat([df1,df2])
print("****************")
print (conc)
print("****************")
"""
    players points  title   player kicks punch
L1  player1      1  Game1      NaN   NaN   NaN
L2  player4      2  Game2      NaN   NaN   NaN
L3  player5      3  Game3      NaN   NaN   NaN
L3      NaN    NaN    NaN  player1     1     1
L4      NaN    NaN    NaN  player4     4     4
L5      NaN    NaN    NaN  player5     5     5
"""

