#formatted string
first_name="john"
last_name="smith"
msg = f'{first_name} {last_name} is a coder'
print(msg)

# Make the String a title 
print (msg.title())

# Make the first letter capital
print (msg.capitalize())

#finds the substring of a string with overlapping occurences
subsCount=0
subs="bob"
s="bobbpbobbobootbobooboobobobbobbbobxboboboopcn"

for i in range(len(s)-len(subs)+1):
        if(s[i:i+len(subs)] == subs ):      
            subsCount+=1
print("Number of times " + subs + " occurs is: " + str(subsCount))

#finds the number of occurences with no overlap
subsCount=0
if (subs in s):
    subsCount = str(s.count(subs)  )
print("Number of times " + subs + " occurs with no overlap is: " + str(subsCount))

#count vowels vs vowels in a string
letter = ''
vowels = 0
cons = 0
s = "This is a string that has vowels and consonants"

for letter in s:
    if ((letter == 'a') or (letter == 'o')or (letter == 'e') 
        or (letter == 'u') or (letter == 'i') ):
        vowels = vowels + 1
    else:
         cons = cons + 1
print ("Number of vowels: " + str(vowels) )

#print all substrings of a string
s = "test"
n = len(s)

for i in range(n): 
        for length in range(i+1,n+1): 
            print(s[i: length])
 
#check if a string is in alaphabetical order           
word = "cab"
res = True
length = len (word)
for i in range(length - 1):
    if word[i] > word[i + 1]:
        res = False
        break
print ("res is " + str(res))


#print the longest alphabetically sorted substring of a string
s = "azcbobobegghakl"
n = len(s)
substrings = []
i=0
for i in range(n): 
    for length in range(i+1,n+1): 
        substrings.append(s[i:length])
i=0
alphabeticalSubstrings = []
for i in range (len(substrings)-1):
    word = substrings[i]
    alphabeticalSubstrings.append(word)
    for n in range(len(word)-1):
        if word[n] > word[n + 1]:
            alphabeticalSubstrings.remove(word)
            break   
longestSubstring = ""
i = 0
n = 0
longestSubstring = max(alphabeticalSubstrings, key = len)        

print ("Longest substring in alphabetical order is: " + str(longestSubstring))

