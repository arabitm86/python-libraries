"""

find secret number using a bisection search

"""
input ("Please think of a number between 0 and 100!")
max = 100
min = 0 
guess = (max+min)//2
notFound = True
while (notFound):    
    print("Is your secret number " + str(int (guess)) + "?")
    response = input ("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

    if (response == "h" ):
        
        max = guess
        guess = (int)((max+min) /2)
         
    elif (response == "l"):
        min = guess
        guess = max / 2
        guess = (int)((max+min) /2)
               
    elif (response == "c"):
        notFound=False
    else:
        print("Sorry, I did not understand your input.")
    
print ("Game over. Your secret number was: " + str(guess))


"""

find the power of a base recursively

"""
def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    if (exp == 1):
        return base
    elif (exp == 0):
        return 1
    else:
        return base * (recurPower(base, (exp - 1)))
                       
print (recurPower (2,5))


"""

Find the power of a number iteratively

"""
def iterPower1(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    ans = 1
    while (exp > 0):
        ans = ans * base
        exp = exp -1
    return ans

print (iterPower1 (2,5))


"""
Find the GCD of two numbers iteratively
"""
def gcdIter(a, b):
    if (a < b):
        count = a
    else:
        count = b
    ans = 1
    for i in range (count,0, -1):
        if ((a % i == 0) and (b % i == 0)):
            ans = i
            break
    return ans 
            
print (gcdIter(17,12))


"""
find the GCD of two numbers recursively

"""
def gcdRecur(a, b):

    if (b == 0):
        return a
    elif (a == 0):
        return b
    else:
        return (gcdRecur(b, a%b))

print (gcdRecur(17,12))


"""
Do a bisectional search to find if a character exists in a string
we sort the string so we can compare the characters and find if 
search for char is bigger or smaller than mid range in array

"""
def isIn(char, aStr):
    aStr_char = sorted(aStr)    
    aStr = "".join(aStr_char)
    #mid_range_char  = aStr[len(aStr) // 2]
    
    if (len(aStr) == 0 or len(aStr) == 1):
        return False
    mid_range_char  = aStr[len(aStr) // 2]

    if (mid_range_char == char):
        return True
    else:
        if (char < mid_range_char):
            return isIn(char, aStr[:len(aStr) // 2])
        else:
            return isIn(char, aStr[len(aStr) // 2:])
        
    return isIn(char, aStr)
    
        
str1 = ""
print (isIn('a', str1))

"""
At the beginning of month 0 (when the credit card statement arrives), assume you owe an amount 
we will call  𝑏0  (b for balance; subscript 0 to indicate this is the balance at month 0).
"""

"""
Any payment you make during that month is deducted from the balance. Let's call the payment 
you make in month 0,  𝑝0 . 
Thus, your unpaid balance for month 0,  𝑢𝑏0 , is equal to  𝑏0−𝑝0 .
"""

"""
𝑢𝑏0=𝑏0−𝑝0
𝑏1=𝑢𝑏0+ 𝑟/12.0 * 𝑢𝑏0
𝑢𝑏1=𝑏1−𝑝1
𝑏2=𝑢𝑏1+𝑟/12.0 * 𝑢𝑏1

Monthly interest rate= (Annual interest rate) / 12.0
Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

          balance = 42
	      annualInterestRate = 0.2
	      monthlyPaymentRate = 0.04
	      
	      # Result Your Code Should Generate Below:
	      Remaining balance: 31.38
"""

"""
find the remaining balance given initial balance, annual interest rate, and
required minimum monthly payment
"""
balance = 484
prevBalance = 0
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
monthlyInterestRate = annualInterestRate / 12 
updated_balance =0


for i in range(0,12):
    
    if (i == 0):
        prevBalance = balance - balance * monthlyPaymentRate
        prevBalance = prevBalance + prevBalance * ( annualInterestRate / 12)
    else:
        prevBalance = prevBalance - prevBalance * monthlyPaymentRate
        prevBalance = prevBalance + prevBalance * ( annualInterestRate / 12)

print ("Remaining balance: " + str(round(prevBalance,2)))

"""
Given a balance do a brute force search to find the montly payment of multiple 10
find the lowest monthly payment to pay off balance in a year
--> this is very slow on big numbers, and multiple of 10 isnt realistic

"""
balance = 3926
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate/12
monthlyPayment = 0
newbalance = balance
while newbalance > 0:
    monthlyPayment += 10
    newbalance = balance
    month = 0

    while month < 12 and newbalance > 0:
        newbalance -= monthlyPayment
        newbalance += (monthlyInterestRate * newbalance)
        month += 1  
    
print ("Lowest Payment:",monthlyPayment)


"""
given a balance, annual interest rate run a bisectional search to find
the monthly payment to pay off balance in a year

"""
balance = 100
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate/12.0
monthlyPaymentLower = balance / 12.0
monthlyPaymentUpper = (balance * (1 + monthlyInterestRate)**12) / 12.0

notFound = True
diff = 0.01

while (notFound):
    unpaidBalance = balance
    minimumMonthlyPayment = (monthlyPaymentUpper + monthlyPaymentLower) / 2
    month =0
  
    while month < 12:
        if ( month == 0):
            unpaidBalance = balance - minimumMonthlyPayment
        else:
            updatedBalance = unpaidBalance + (monthlyInterestRate * unpaidBalance)
            unpaidBalance = updatedBalance - minimumMonthlyPayment        
        month+=1
    
    if unpaidBalance < 0 and abs(unpaidBalance) > diff :
        monthlyPaymentUpper = minimumMonthlyPayment
        minimumMonthlyPayment = (monthlyPaymentLower + minimumMonthlyPayment) / 2
    elif unpaidBalance > 0 and abs(unpaidBalance) > diff:
        monthlyPaymentLower = minimumMonthlyPayment
        minimumMonthlyPayment = (monthlyPaymentUpper + minimumMonthlyPayment) /2
    else:
        notFound = False
        break
print ("Lowest Payment: " + str(round(minimumMonthlyPayment,2)))       


         
    
