class Employee:
     def __init__(self, id=None,first=None, last=None, pay=0.00):
          self.firstName = first
          self.lastName = last
          self.eid = id
          self.hpr = pay

     def setEid(self, id):
             self.eid = id

     def getEid(self):
        return self.eid
     
     def setFname(self, first):
        self.firstName = first

     def getFname(self):
        return self.firstName

     def setLname(self, last):
        self.lastName = last

     def getLname(self):
        return self.lastName
    
     def setHpr(self, pay):
        self.hpr = pay

     def getHpr(self):
        return self.hpr

     def pay(self, totalHrs):
        if(totalHrs <= 40.0):
            return self.hpr * totalHrs
        else: 
            wkPay = self.hpr * 40
            wkPay += (self.hpr * 1.5) * (totalHrs - 40)
            return wkPay    

eid = int(input("Employee ID number: "))
fName = str(input("Employee First Name: "))
lName = str(input("Employee's Last Name: "))
hpr = float(input("Employee's Hourly Wage: "))
totalHrs = float(input("Enter " + fName + " " + lName + " total hours worked: "))

newEmp = Employee(eid,fName,lName,hpr)
paycheck = newEmp.pay(totalHrs)
print("{0} {1}'s paycheck this period is ${2:.2f}".format(newEmp.getFname(),newEmp.getLname(),paycheck))