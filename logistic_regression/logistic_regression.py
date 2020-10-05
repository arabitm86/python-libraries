"""
1. Undertand the variables
2. Plot the labeled data
3. Draw regression curve
4. Find out the best fitted curve using Maximum Likelihood Estimator (MLE)
"""

"""x = (1, 2, (3, 'John', 4), 'Hi')
print (str(x [-1]))
print (str(x [-1][-1]))
print (str(x [0:-1])) # (all of it)
print(str(len (x)))
print (2 in x)
y = [1,2,3]
print (str(y [-1]))"""


count = 0
"""tup = ()

for i  in range (len(z)):
    if i % 2 == 0:
        tup = tup + (z [i],)
print (tup)
"""
def oddTuples(aTup):
    tup = ()
    for i  in range (len(aTup)):
        if i % 2 == 0:
            tup = tup + (aTup [i],)
    return tup

def oddTuples1(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # a placeholder to gather our response
    rTup = ()
    index = 0

    # Idea: Iterate over the elements in aTup, counting by 2
    #  (every other element) and adding that element to 
    #  the result
    while index < len(aTup):
        rTup += (aTup[index],)
        index += 2

    return rTup

t = ('I', 'am', 'a', 'test', 'tuple')
z = ('I', 'am', 'a', 'test', 'tuple', 'test', 'test1')
print (oddTuples((3, 18, 17, 20, 5, 20, 20, 17)))
print (oddTuples1((3, 18, 17, 20, 5, 20, 20, 17)))
