# Python provides a built-in method called random.shuffle that will shuffle the list data type.  Do not use this.
# For this assignment, you are to create your own shuffle algorithm that will take as input a sorted list and randomly shuffle the items before returning the list.  Try to make your algorithm as efficient as possible.
# Add a comment to your code stating what the time complexity of your algorithm is and why.
# Display list before and after shuffle.  Call your shuffle function multiple times, each time on the original sorted list to show the random order of the list items.

data = [7, 20, 26, 31, 40, 51, 55, 63, 74, 81]
ndata = len(data)
import random

def shuffleAlgorithm(data, ndata):
    for i in range(ndata-1, 0, -1):
        r = random.randint(0, i +1)
        data[i], data[r] = data[r], data[i]
    return data 

print(data)
print(shuffleAlgorithm(data,ndata))
print(shuffleAlgorithm(data,ndata))
print(shuffleAlgorithm(data,ndata))
print(shuffleAlgorithm(data,ndata))

# fisher yates algorithm - O(n) time complexity because i'm not creating a copy of the list to shuffle through it. 
# instead i'm modifying the list in place or at a 'constant space' making it O(n)
# swapping the last item with a random -not previously selected- item and repeating until all items in list have been selected