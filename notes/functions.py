"""
A function is a block of code that exist within a program designed to perform a specifc task.
When defining the name of a function, you must follow the same naming rules as those for variables.
There are rules when naming functions / variables and include:
• You cannot use one of Python’s key words as a functions / variable name. 
• A functions / variable name cannot contain spaces.
• The first character must be one of the letters a through z, A through Z, or an underscore character (_).
• After the first character you may use the letters a through z or A through Z, the digits 0 through 9, or underscores.
• Uppercase and lowercase characters are distinct. 

To create a function we use key word def (definition) followed by name of the function 
a set of parenthesis and a colon.
"""
def classMessage(): #function name is classMessage here
     print("AFS-210", end=" : ") #this line tells intepreter where to begin and end the code for this function.. 
     print("Data Structures and Algorithms")
     
#to execute the function:
print("Welcome to:")
classMessage()
print("I hope you enjoy your next eight weeks of class.")

"""
make use use variables globally or locally
local variable is created within the function and is not accessible outside of the function
globally variable is created outside of the function and remain until the function is completed
"""
applesSold = 10
applePrice = 0.20
def showAppleTax():
     taxRate = 0.08
     appleTax = (applesSold * applePrice) * taxRate
     print("The tax on the sale of",applesSold,"apples is",appleTax)
     print("The total for ",applesSold,"apples is $",applesSold + appleTax," due at checkout.")
showAppleTax()
print(applesSold)

print("-----------------------------------------------------")
def showSum(a,b):
     print(a+b)
x = 1
y = 3
showSum(x,y)

#to avoid errors when no input by user, use the following
def showSum(a,b=0):
     print(a+b)
x = 1
y = 3
showSum(x,y)
showSum(x)

#to return values from a function use key word return
def sum(a,b):
     return a+b
y = sum(1,2)
print(y)

#returning more than one value from a function
def ops(a,b):
     return a+b,a-b, a*b, a/b
sum, sub, mul, div = ops(1,2)
print(sum)
print(sub)
print(mul, "," , div)
