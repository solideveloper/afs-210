"""
Given: 
     Data1 = 7, False, "Apple", True, 7, 98.6
     Data2 = "July", 4, 8, "Tango", 4.3, "Bingo"
     Data3 = "A", 7, -1, 3.14, True, 7  
     Data4 =  "name" = "Joe",  "age" = 26,   "active" = True,  "hourly_wage" = 14.75
     
In your Week 2 folder, create a file called datastructures.py
The datastructures.py will store the data sets listed below in one of four built-in Python data structures (lists, tuples, sets, dictionaries)
You will need to choose the appropriate data structure for the data provided and for the tasks that must be performed on each data set.  You can only use each data structure once.
Complete each given task for each of the data sets.
"""
#Tuple
Data1 = (7, False, "Apple", True, 7, 98.6)
#Count the number of items:
print(len(Data1))
#find the value of the fourth item stored in the data set
print(Data1[3])
# count the number of times 7 appears
print(Data1.count(7))

#Set
Data2 = {"July", 4, 8, "Tango", 4.3, "Bingo"}
#Remove a random element from the data set
Data2.pop()
print(Data2)
#Add "Alpha to the data set"
Data2.add("Alpha")
#print data set
print(Data2)

#List
Data3 = ["A", 7, -1, 3.14, True, 7]
#Print the data set in reverse order
Data3.reverse()
#Change 2nd value in data set to 'B'
Data3[1]="B"
#remove the last item and print the data set
Data3.pop()
print(Data3)

#Dictionary
Data4 = { "name": "Joe", "age": 26, "active": True, "hourly_wage": 14.75 }
#change "active" state to False
Data4["active"] = False
#Add "address" with a value of "123 West Main Street"
Data4["address"] = "123 West Main Street"
#Print weekly salary for Joe if he worked a full 40hr week
hours_worked = Data4["hourly_wage"] * 40.0
print("Joe's Weekly Salary is: $"+"{:.2f}".format(hours_worked))
#print the data set
print(Data4)
