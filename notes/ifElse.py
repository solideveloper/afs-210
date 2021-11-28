""""
Operator Meaning
> Greater than
< Less than
>= Greater than or equal to
<= Less than or equal to
== Equal to
!= Not equal to

A control structure is a logical design that controls the order in which 
a set of statements are executed. In Python, the statements are executed in 
sequential structure by default (top to bottom- the order they appear in)

the if statement creates a decision structure which allows program to have
more than one path of execution. then indent new decision structure 
under the if statement to create block of code.
"""

# >=greater  <=less  , qnty is the parameter here
def buy2Get1Free(qnty):
     if qnty >= 3:
	     print("You qualify for the Buy 2 Get 1 Free Discount")
     else:
     		print("You do not quality for the discount")
applesSold = 1
buy2Get1Free(applesSold)
applesSold = 3
buy2Get1Free(applesSold)