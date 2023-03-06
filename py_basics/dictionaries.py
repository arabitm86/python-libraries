"""
Values in dictionary can be any type
Values for different keys can be the same
Values can even be dictionaries or lists

Keys:
- must be unique
- must be immutable type: int, float, string, tuple, bool so we cant
change the key and expect to find the value later

No order to keys or values 
"""

#empty dictionary
my_dict = {}

#dont rely on order, get w/ key -- can NOT have duplicate keys
grades = {"Anna":"B", "Touf":"A", "Katy":"C", "Mike":"A"}

print (len(grades))

print(grades)
#if there is no key = error
print(grades["Anna"])

#Find if a key is there
print ("john" in grades)

#remove entry
del(grades["Anna"])

#get set of keys --> returns tuple
print(grades.keys())

#get all the values
print(grades.values())


animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

animals['a'].append('donkey')
animals['a'].append('dog')
animals['a'].append('dingo')

print(len(animals.values()))

count = 0

for item in animals:
    count+= len(animals[item])

print ("total items is "  +str(count))

def how_many(aDict):
    total = 0
    for item in aDict:
        total+= len(aDict[item])
    return total
        
print ("total items is "  +str(how_many(animals)))
   
print (animals)     
def biggest(aDict):
    
    biggest_size = 0
    biggest = ""
    for item in aDict:
        if (len(aDict[item]) > biggest_size):
            biggest_size = len(aDict[item])
            biggest = item
    
    return biggest

print(biggest(animals))
        
#some cool formatting with string below        
dictionary = {
    "0" : "Zero",
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "10": "Ten"
    } #key value pairs, keys need to be unique

phone_number = input ("Phone:")
numbers_to_words = ""
for character in phone_number:
    numbers_to_words = f'{numbers_to_words}{dictionary.get(character)} '
print (numbers_to_words)


