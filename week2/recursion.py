def loop1():
    # Sum of odd numbers between 1 and 20
    odd_sum = 0
    for i in range(20):
        if (i % 2) == 1:
            odd_sum += i
    return odd_sum
print(loop1())

""" 
to turn the above iterative loop into the below iterative loop
we are doing the following:
passing in numbers to parameters num = 20 and the odd_sum
    this is an accumulator thats being carried thru each call as we make recursive calls over and over
the base case is if num is less than or equal to 1. This is so that our loop stops when we get to 1
    if we do not include a base case then we'll create an endless or infinite loop 
(   an infiite loop stops only when you run out of applicable memory)
then we take that number and add it to odd_sum and return that odd_sum back through
if num is greater than 1 and the number is odd then we add that number to the odd sum
then we return the next which is a call to ourself (always have to call urself in recursive function)
and 2nd is move toward base case. in this case num-1 w/ base case of 20  

"""
def loop1Rec(num=20, odd_sum=0):
         # Duplicate the loop1 function using recursion
    if num <= 1:
        odd_sum += num
        return odd_sum
    elif num % 2 == 1:
        odd_sum += num
    return loop1Rec(num-1, odd_sum)
print(loop1Rec())

"""
An alternate way to write the above recursive function that doesn't carry the results between calls is the following:
"""
def loop1Recursion(num):
    if num == 0:
        return num
    elif num % 2 == 1:
        return num + loop1Recursion(num-1)
    else:
        return loop1Recursion(num-1)
print(loop1Recursion(20))
        

def loop2():
         # Sum of even numbers between 1 and 20
    i = 0
    even_sum = 0
    while i < 20:
        if (i % 2) == 0:
            even_sum += i
        i += 1
    return even_sum
print(loop2())

def loop2Rec(num=0, even_sum=0):
    # Duplicate the loop2 function using recursion
    if num >= 20:
        return even_sum
    elif num % 2 == 0:
        even_sum += num
    return loop2Rec(num+1, even_sum)
print(loop2Rec())

