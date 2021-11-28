"""  <-- use to create notes in .py files

Python offers the following math operator.

Symbol		Operation			Description
----------------------------------------------
+ 			Addition 			Adds two numbers
_ 			Subtraction 		Subtracts one number from another
* 			Multiplication 	Multiplies one number by another
/ 			Division 			Divides one number by another and gives the result as a floating-point number
// 			Integer division 	Divides one number by another and gives the result as an integer
% 			Remainder 		Divides one number by another and gives the remainder
** 			Exponent 			Raises a number to a power
"""
print(10 + 5)
print(11 - 5)
print(4 * 3)

#a decimal will always display as a float
print(6 / 2)

#this will retrun the result as an integer without the remainder
print(15 // 6 )

#this will divide one number by the other and return ONLY the remainder
print(15 % 6)

#to raise a number to a power
print(2 ** 3)
print('---------------------------------------------')

#mathOps with variables can also be done and will return a float
applesSold = 50
applePrice = 0.20
print(applesSold * applePrice)
print(applesSold + applePrice)

# + operator used with two strings = string concatenation (combining two strings by appending one to the other)
x = "Hello"
y = "World"
z = x + " " + y
print(z)
#or
x = "5"
y = "seven"
z = x + " " + y
print(z)




