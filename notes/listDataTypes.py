"""
List items are ordered, changeable, and allow duplicate values.
List items are indexed with the first item having an index of [0], the second item has an index of [1] etc.
The list is mutable (ie: changeable), meaning that we can change, add, and remove items in a list after it has been created.
A list may contain multiple different DataTypes include integers, strings, floats, booleans, lists and objects
Lists are created by placing a sequence of values inside square brackets []
"""
progLang = ["python", "c#", "javascript", "java", "c++"]
moreLang = ["rust", "php", "perl", "ruby", "go"]

myNumbers = [1,2,3,4,5]
myFloats = [1.0, 2.1, 3.2, 4.3]

myMixed = ["Hello", True, 6, ["item1","item2","item3"], 3.14]

print(progLang)
progLang.append("c")
print(progLang)

progLang.extend(moreLang)
print(progLang)

progLang.insert(1, "reactjs")
print(progLang)

#to remove list items
progLang.remove("reactjs")
print(progLang)

#pop will remove last item in list unless index specified
progLang.pop()
print(progLang)
progLang.pop(6)
print(progLang)

#to find index number of list item
print(progLang.index("php")) #

#to tell me how many items on my list
print(len(progLang))

# to count how many instances of a word or letter in list use count
print(progLang.count("php"))
progLang.append("php")
print(progLang)
print(progLang.count("php"))

#to sort the list
progLang.sort()
print(progLang)
#to sort in reverse
progLang.sort(reverse=True)
print(progLang)
#sorting only works if datatypes match. (will not work on myMixed list)

#print an item from another list to a list
print(myMixed[3],[2])
print("--------------------------------")
print(myMixed[2],progLang[4])