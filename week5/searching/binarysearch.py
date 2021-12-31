""" 
Searching is the algorithmic process of finding a particular item in a collection of items
a search typically answers true or false as to whether an item exists in the collection
it may be modified to return where the item is found or 
return the item itelf if searching based on 1 data element of a multi-data element

"""

list1 = [7, 20, 26, 31, 40, 51, 55, 63, 74, 81]
list2 = [7, 20, 26, 31, 40, 51, 55, 63, 74, 81]
list3 = ["Alpha", "Beta", "Delta", "Epsilon", "Gamma", "Theta", "Zeta"]

def binarySearch(list, data):
    start, end = 0, (len(list)-1)
    while start <= end:
        mid = (start + end) //2
        if data ==list[mid]:
            return True
        if data > list[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return False

print(binarySearch(list1, 31))
print(binarySearch(list2, 77))
print(binarySearch(list3, "Delta"))