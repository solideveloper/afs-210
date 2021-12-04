class Employee:
     def __init__(self,eid,fName,lName,hpr):
          self.fName = fName
          self.lName = lName
          self.eid = eid
          self.hpr = hpr
     def pay(self, hrsWrkd):
          self.hrsWrkd = hrsWrkd
          if hrsWrkd <= 40.0:
            return self.hpr * hrsWrkd
          if hrsWrkd > 40: 
            wkPay = self.hpr * 40
            wkPay += (self.hpr * 1.5) * (hrsWrkd - 40)
            return wkPay    

eid = int(input("Employee ID number: "))
fName = str(input("Employee First Name: "))
lName = str(input("Employee's Last Name: "))
hpr = float(input("Employee's Hourly Wage: "))
hrsWrkd = float(input("Enter " + fName + " " + lName+"\'s" + " total hours worked: "))
newEmp = Employee(eid,fName,lName,hpr)

print("Employee No.",eid,fName,lName+"\'s", "paycheck for this period is $""{:.2f}".format(newEmp.pay(hrsWrkd)))


# syntax for currency_format = "${:,.2f}".format(yearlySalary)
# print(currency_format)