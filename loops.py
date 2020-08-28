iteration = 0
count = 0
while iteration < 5:
    for letter in "hello, world":
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 
    
count = 0
phrase = "hello, world"
for iteration in range(5):
    index = 0
    while index < len(phrase):
        count += 1
        index += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    
    
count = 0
phrase = "hello, world"
for iteration in range(5):
    while True:
        count += len(phrase)
        break
    print("Iteration " + str(iteration) + "; count is: " + str(count))


s ="eiouamn"

letter = ''
vowels = 0
cons = 0

for letter in s:
    if ((letter == 'a') or (letter == 'o')or (letter == 'e') 
        or (letter == 'u') or (letter == 'i') ):
        vowels = vowels + 1
    else:
         cons = cons + 1
print ("Number of vowels: " + str(vowels) )

s = "oobobbobobobob"
subs = "bob"
subsCount = 0
if (subs in s):
    subsCount = str(s.count(subs)  )

print("Number of times " + subs + " occurs is: " + str(subsCount))

subsCount=0
length  = len(s)
print (str(length))
for i in range(len(s)-len(subs)+1):
        if(s[i:i+len(subs)] == subs ):      
            subsCount+=1
print("Number of times " + subs + " occurs is: " + str(subsCount))