class Employee():
     global first_name, last_name
     global last_name
     
     employeeId = input('Enter Employee ID: ')
     first_name = str(input('Enter Employee  First Name: '))
     last_name = str(input('Enter Employee Last Name: ' ))
     hpr = float(input('Enter Employee Hourly Pay Rate: '))
     hrsTotal= float(input('Enter Employee total hours (with overtime): '))
     
     def pay(hrsTotal, hpr,):
          if(hrsTotal <= 40.0):
              pay = float(hrsTotal * hpr)
              return print(first_name + " " + last_name + "\'s" + " paycheck is $" + str(pay) + " for " + str(hrsTotal) + " Regular Hours.")
          elif(hrsTotal > 40.0):
               reg_pay = float(hrsTotal * hpr)
               overtime = float(hrsTotal - 40.0)
               ot_pay = float(overtime * (hpr * 0.5))
               paycheck = float(reg_pay + ot_pay)
               return print(first_name + " " + last_name + "\'s" + " paycheck is $" + str(paycheck) + ' with 40.0 Regular Hours, and ' + str(overtime) + ' hours of Overtime.')
     pay(hrsTotal, hpr)