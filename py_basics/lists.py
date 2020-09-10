L = [2,1,3]

# add element to the end of the list, mutate list
L.append (4)

#returns a list of the first element
print (L[0:1])

L1 =  [2,1,3]
L2 = [4,5,6]

# concatenate lists, like tuples
L3 = L1 + L2

#append more than 1 element with extend
L3.extend([0,6])

print (L3)

# removes the first occurence of an element, and if it cant it returns an error
L3.remove(3)
print (L3)

#removes the element at index
del(L3[3])
print (L3)

#removes the last element
L3.pop()
print (L3)

#we can go back and forth between strings and lists
str1  = "Thisisgreat"
print (list(str1))

#split a string on a character and return a list of two items
str1 = "I <3 CS"
l = str1.split('<')
print (l)

#go from a list to a string
L4 = ['a', 'b', 'c']
str2 = ''.join(L4)
print (str2)

#convert to a string and merge each item and insert a char
str2 = '_'.join(L4)
print (str2)

#we can sort a list and not mutate it
L5 = [2,1,5,3,9]
sorted(L5)
print (L5)

#we can sort a list and not mutate it
L5 = [2,1,5,3,9]
L5.sort()
print (L5)

listA = [1, 4, 3, 0]
listB = ['x', 'z', 't', 'q']

#returns a function
listA.sort

#return none, sorts original list
listA.sort()

#return none, mutate listA and insert 100 in 0th index
listA.insert(0, 100)

#returns none, remove the first occurence of 3, mutate list
listA.remove(3)

#returns none, adds number 7 to the end
listA.append(7)

#returns a list, concatenate list A and B
listC = listA + listB

#first returns none, sorts ListB, second returns string which is Z, last element
listB.sort()
listB.pop()

#count occurences of a, return number = 0
listB.count('a')

#no a to remove, returns error
#listB.remove('a')

#adds these elements to the list, returns nontype since it mutates
listA.extend([4, 1, 6, 3, 4])

#returns number = 4, number of occurences of number 4
listA.count(4)

#returns the index of the number 1
listA.index(1)

#returns the element it popped at index location given
listA.pop(4)

#reverses the list, mutates it, returns none
listA.reverse()

#aliases
warm = ['red', 'yellow', 'orange']

hot = warm
#both warm and hot are binded to the same place, changing one changes the other
hot.append("green")
print (warm)

#cloning list
aList = hot[:]
aList.append("black")
print (hot)
print (aList)

#list of lists --> changing the initial list, trickles into list of list
listofLists = [hot]
listofLists.append(["lightblue"])
print (listofLists)

hot.append("pinkish")
print (listofLists)

#Generalization of hops -- Uses MAP

for e in map (abs, [1,-2,-3,-4]):
    print (e)

#using an n-ary function
L1 = [1, 22, 90]
L2 = [5, 21 , 91]
for e in map (min, L1, L2):
    print (e)


testList = [1, -4, 8, -9]

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
    return L
        
def absSquared (x):
    x = abs(x)
    x = x**2
    return x
 
print(applyToEach(testList, absSquared))