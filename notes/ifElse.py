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
     if qnty >= 6:
	     print("You qualify for the Buy 2 Get 1 Free Discount")
# to have more that one else if/else statement we use elif statement. 
# it must go after the if and before the last else
     elif (qnty >= 3) and (qnty < 6):
     	print("You get one Apple for Free!")
     else:
     	print("You do not quality for the discount")
applesSold = 1
buy2Get1Free(applesSold)
applesSold = 3
buy2Get1Free(applesSold)
applesSold = 4
buy2Get1Free(applesSold)
applesSold = 6
buy2Get1Free(applesSold)