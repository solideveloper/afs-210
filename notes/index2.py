#print function is used to display output to the user
#data type passed is string (string literal - and must be in '' or "" marks)
print('---------------------------------------------')
print('This is afs210 python review')
print('---------------------------------------------')

#to print ""/'' within a string simply:
print('Quote your words "like this" okay?')
print("or you can do it 'this way' okay?")
print("You can also \"do this\" which looks cool in vsc")
print("""or you can do "this" weird looking way""")     
print('''or you can do 'this' weird looking way''') 
print('---------------------------------------------')


#how to create a string with assigned variables
applesSold = 10
applePrice = 0.20
print("We sold",applesSold," apples at $",applePrice,"each for a total of $",(applesSold * applePrice))

#to remove separator, use sep=""
print("We sold",applesSold,"apples at $",applePrice,"each for a total of $",(applesSold * applePrice), sep="")
#change your separator with sep="-" or sep="." etc
print("We sold",applesSold,"apples at $",applePrice,"each for a total of $",(applesSold * applePrice), sep="-")
print('---------------------------------------------')
#change amount of decimal places with format specifier:
applesSold = 5000
applePrice = 0.20
print("We sold ",applesSold," apples at $",
format(applePrice,',.2f'),\
# ',.2f' the comma means include this separator, the .2 means add 2 decimal places, the f means display as float
" each for a total of $",\
format((applesSold * applePrice),',.2f'),\
sep="")
print('---------------------------------------------')

#to prompt user input we use the input function. This will ALWAYS be a string. 
applesSold = int(input("How many apples did you sell this week? "))
#int here means the user MUST input an integer (this can be a positive or negative number but NOT a word)
applePrice = float(input("What the price of each apple sold? "))
#float here means the user may input an integer with a decimal 
print("You sold ",applesSold," apples at $",applePrice," each for a total of $",(applesSold * applePrice), sep="")
print('---------------------------------------------')

