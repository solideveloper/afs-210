"""
variables are used to store variables in the computers memory. 
we use an assignment statements to create variables 
we use assignment statements to reference a piece of data. 
variable names cannot contain spaces
variable names are case sensitive
"""

applesSold = 10 
"""
applesSold=10 is the assignment statement.. 
the = sign is the assignment operator.
applesSold is the variable name
applesSold is now pointing to the memory location/reference of where 10 is stored in memory.
**We are not actually assigning applesSold to the value of 10. We're assigning applesSold to the memory location of where 10 is located at in memory**
 
"""

a = 5
# a now = memory location of where 5 is stored
b = a
# now b = same memory location of where a is stored
a = 7
# a = memory location of where 7 is stored

print(a)
print(b)



c = 5 
print(c)
print(type(c))
# c will print as an integer

d = 5.0
print(d)
print(type(d))
# d will print as a flaot

a = "True"
print(a)
print(type(a))
# a will print as a string because it is in quotes

a = True
print(a)
print(type(a))
# a will return a boolean of true here

