""""
In object oriented programming, classes provide a means of bundling data 
and functionality together. Creating a new class creates a new type of object
aligning new instances of that type to be made.
The simplest form of class definition looks like this:
class ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>
"""
#example
class dog:
    def __init__(self, name, breed, age, color, size):
        self.name = name
        self.breed = breed
        self.age = age
        self.color = color
        self.size = size
    def bark(self):
        print("Woof..Woof")
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name
    def getAge(self):
        return self.age
    def setAge(self,age):
        self.age = age

dog1 = dog("Lancelot","German Shepherd",2,"brown","large")
dog2 = dog("Nugget","Poodle",4,"blonde","medium")
dog3 = dog("Chico","Chihuahua",1,"tan","small")

print(dog1.getName())
print(dog1.bark())
print(dog1.setAge(3))
print(dog1.getAge())