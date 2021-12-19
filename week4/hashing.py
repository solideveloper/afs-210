# Write the missing code in the HashTable class for the following methods:
# hashfunction
# rehash
# put
# get
# Create a hash table with a size of 10.
# The primary hash function will use key modulus table_size
# Resolve collisions using double hashing where the secondary hash function is key div table_size where div is integer division (//)
#  Note that the double hashing algorithm used is not perfect and there may be unresolved collisions where data is lost.  
# Store the items in the table below
# Print the slots
# Print the data
# Print the value of the data for key 52
# Challenge: Create a new secondary hash function using your own algorithm that avoids all collisions with this data set.
#  Challenge: Print the updated slots
#  Challenge: Print the updated data

class HashTable:
    def __init__(self) -> None:
        self.size = 10
        self.slots = [None] * self.size #old keys
        self.data = [None] * self.size

    def hashfunction(self,key): #this is my primary hash function
        return key % self.size #key modulus table size

    def rehash(self,key):
        # key div table_size where div is integer division (//)
        return key // self.size
        # Note that the double hashing algorithm used is not perfect and 
        # there may be unresolved collisions where data is lost.  

    def put(self,key,data):
        valueOfHash = self.hashfunction(key)
        if self.data[valueOfHash] == None:
            self.slots[valueOfHash] = key
            self.data[valueOfHash] = data
        else:   #what if it's not equal to none...
            # when slot is occupied but doesn't collide = Update:
            if self.slots[valueOfHash] == key:
                self.data[valueOfHash] = data
            # when slot is occupied & has same value = Collision and need to reshash:
            valueOfHash = self.rehash(key)
            if self.data[valueOfHash] == None:
                self.data[valueOfHash] = data
                self.slots[valueOfHash] = key
            else: 
                return None
    def get(self,key):
        #if slot matches your key then get that value and return the data
        # otherwise rehash and return the data
        valueOfhash = self.hashfunction(key)
        return self.data[valueOfhash]
        # Insert your code here to get data by key

    def __getitem__ (self,key):
        return self.get(key)

    def __setitem__ (self,key,data):
        self.put(key,data)


H = HashTable()
H[69] = 'A'
# Store remaining input data:
H[66] = 'B'
H[80] = 'C'
H[35] = 'D'
H[18] = 'E'
H[52] = 'F'
H[89] = 'G'
H[70] = 'H'
H[12] = 'I'

# print the slot values
print(H.slots)
# print the data values
print(H.data)
# print the value for key 52
print(H[52])


