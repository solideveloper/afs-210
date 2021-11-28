"""
There are two categories of loops:
condition controlled: a true/false condition to control the number of times it repeats
count controlled: repeats a specific number of times.
we use a for statement to write a count controlled loop
the for statement is designed to work with a sequence of data

for <variable> in [sequence of data]:
"""


def countDown():
     for currentCount in [5, 4, 3, 2, 1]:
          print(currentCount)
     print("BLAST OFF!")
     countDown()

print("-------------------------------------")

"""
if we dont know the sequence of data before hand, 
we can pass items into the function
"""
def welcomeGuests(guestNames):
     for guest in guestNames:
          print("Welcome",guest)
guests = []
guests.append(input("Please enter the name of a guest: "))
guests.append(input("Please enter the name of a guest: "))
guests.append(input("Please enter the name of a guest: "))
welcomeGuests(guests)
print("---------------------------------")

"""
To provide starting number for the starting number of the count use python range function
range function takes 1, 2 or 3 arguments.
range(start, stop[, step])
start = The value of the start parameter (or 0 if the parameter was not supplied)
stop = The value of the stop parameter
step = The value of the step parameter (or 1 if the parameter was not supplied)
"""
def count(stop):
     for number in range(1, stop+1, 1):
          print(number)	
stoppingNum = int(input("Count to? "))
count(stoppingNum)

""" 
To redefine countdown function
"""
def countDown(start):
     for currentCount in range(start,0,-1):
          print(currentCount)
     print("BLAST OFF!")
startingNum = int(input("Enter the countdown starting number: "))
countDown(startingNum)
print("---------------------------------")

"""
 in Python we use WHILE statement to write a condition control loop
"""
def countDown(start):
     while start > 0:
          print(start)
          start -= 1
     print("BLAST OFF!")
startingNum = int(input("Enter the countdown starting number: "))
countDown(startingNum)

# another example
def countDown(start):
     continueLoop = True
     while continueLoop:
          print(start)
          start -= 1
          if (start == 0):
               print("BLAST OFF!")
               continueLoop = False	
startingNum = int(input("Enter the countdown starting number: "))
countDown(startingNum)

# another example
def countDown(start):
     while True:
          print(start)
          start -= 1
          if (start == 0):
               print("BLAST OFF!")
               break #break is stopping the loop here
startingNum = int(input("Enter the countdown starting number: "))
countDown(startingNum)
