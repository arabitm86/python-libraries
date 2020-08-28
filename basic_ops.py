
x=3
y=5
z=7

# basic if else
if (x < y) & (x < z): 
   print ("x is least")
elif (z > y):
   print ("z is biggerst")
else:
    print ("y is in the middle")

#boolean and float
a=3
print(a == 5.0)
a=2.6
print (int(a))
print (5/2)

# string/array manipulation
str0 = 'hello'*3
print (str0 + " " + str(len(str0)))
print (len(str0))
print ("\nitem 0 of str is " + str0[0] )
print("\nstr range of 3-7 is " + str0[2:6])
print("\nstr range of 1-end is " + str0[1:])
print("\nget a copy of str " + str0[:])
print ("abcd"[2])
print ("abcd"[0:2])
print ("abcd"[:2])
print ("abcd"[2:])

str1 ='hello'
print (str1)
print ("HELLO" == str1)
str3 = "world"
print ('a' in str3)
str4 = str1 + str3
print ("low" in str4)
print (str3[:-1])
print (str1[1:])
print (str4[1:9:2]) #skip 2
print (str4[::-1])  #backwards

#loops
n=0
while (n < 5):
   print (n)
   n = n+1
   
print("\n")
n=0
for n in range (5):
   print (n) 

mysum=0
for i in range(7,10): # when its equal or greater than 10 it breaks 
  mysum += i
print (mysum)

mysum=0
for i in range(5,11,2): #when i is equal or greater than 11 it breaks
  mysum += i
print (mysum)

mysum = 0
for i in range (5, 11, 2):
   mysum += i
   if mysum ==5:
      break
print (mysum)  # prints 5


num = 0
while num <= 5:
    print(num, end = '')
    num += 1
print()
print("Outside of loop")
print(num) 
print ("================")

n=0
while (n < 10):
  n = n+2
  print (n)
print ("Goodbye!")

print ("================")
print ("Hello!")
n = 10
while (n >= 2):
  print (n)
  n = n-2

print ("================")
addition = 0
end = 6
i =0
while ( i <= end):
   addition = addition + i
   i = i + 1
print (addition)

print ("================")
end =6
addition =0
for n in range (0,end+1):
    addition = addition + n
print (addition)

print ("================")
i=12
for n in range (0,10):
  i = i-2
  if (i < 2):
     break
  print (i)
print ("Goodbye!")

print ("================")
num = 10
for num in range(5):
    print(num)
print(num)

print ("================")
print ("Vowels + Constants counter for string below")
school = 'Massachusetts Institute of Technology'
numVowels = 0
numCons = 0

for char in school:
    if char == 'a' or char == 'e' or char == 'i' \
       or char == 'o' or char == 'u':
        numVowels += 1
    elif char == 'o' or char == 'M':
        print(char)
    else:
        numCons -= 1
print('numVowels is: ' + str(numVowels))
print('numCons is: ' + str(numCons)) 
