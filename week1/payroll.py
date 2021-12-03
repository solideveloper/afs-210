class Employee:
     def __init__(self,eid,fName,lName,hpr):
          self.fName = fName
          self.lName = lName
          self.eid = eid
          self.hpr = hpr


     def pay(self, totalHrs):
          self.totalHrs = totalHrs
          if totalHrs <= 40.0:
            return self.hpr * totalHrs
          if totalHrs > 40: 
            wkPay = self.hpr * 40
            wkPay += (self.hpr * 1.5) * (totalHrs - 40)
            return wkPay    

eid = int(input("Employee ID number: "))
fName = str(input("Employee First Name: "))
lName = str(input("Employee's Last Name: "))
hpr = float(input("Employee's Hourly Wage: "))
totalHrs = float(input("Enter " + fName + " " + lName+"\'s" + " total hours worked: "))
newEmp = Employee(eid,fName,lName,hpr)

print("Employee No.",eid,fName,lName+"\'s", "paycheck this period is $""{:.2f}".format(newEmp.pay(totalHrs)))

# currency_format = "${:,.2f}".format(yearlySalary)
# print(currency_format)