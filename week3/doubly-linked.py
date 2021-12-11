class Node:
    # A doubly-linked node.
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    # A doubly-linked list.
    def __init__(self):
        # Create an empty list.
        self.tail = None
        self.head = None
        self.count = 0

    def iter(self):
        # Iterate through the list.
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val


    def size(self) -> int:
        return self.length()

    def length(self):
        # Returns the number of elements in the list
        return self.count


    def addFirst(self, data) -> None:
        newNode = Node(data)
        self.count += 1
        if (self.head == None):
            self.head = newNode
            self.tail = newNode
        else: 
            newNode.next = self.head
            self.head.prev = newNode 
            self.head = newNode


    def addLast(self, data) -> None:
        node = Node(data)
        self.count += 1
        if (self.head == None):
            self.tail = node
            self.head = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
  
    # Add a node to the list at the given index position
    # If index equals to the length of linked list, the node will be appended to the end of linked list
    # If index is greater than the length, the data will not be inserted.
    # This function does not replace the data at the index, but pushes everything else down.
    def addAtIndex(self, data, index):
        newNode = Node(data)
        if(index == 0):
            self.addFirst(newNode)
        if(index == self.count):
            self.addLast(newNode)    
        if(index > self.count):
            print("index does not exist")
        else:
            current = self.head
            for _ in range(index):  #underscore _ denotes a “discarded” value. “Discarded” meaning that you don’t intend to use the loop counter value within the loop, so you don’t declare a variable.
                current = current.next
                
            newNode.next = current.next
            newNode.prev = current
            if current.next:
                current.next.prev = newNode
            current.next = newNode
            self.count += 1 


    def indexOf(self, data):
        search = self.head
        result = 0
        i = 0
        if(search != None): #search only if list has items
            while(search != None): #while searching
                i+=1 #add 1
                if(search.data == data): #if search returns data
                    result+=1 # include result 
                    break
                search = search.next 
            if(result == 1):
                return i
            else:
                return -1
        else: #if list doesnt have items
            return -1 

    def add(self, data) -> None:
        # Append an item to the end of the list
        self.addLast(data)

    def clear(self) -> None:
        # Remove all of the items from the list
        self.head = None
        self.tail = None
        self.count = 0

    def deleteAtIndex(self, index) -> None:
        # Delete the node at the index-th in the linked list, if the index is valid.

        if (index > (self.count-1)):
            return
            
        curr = self.head
        prev = self.head

        for n in range(index):
            prev = curr
            curr = curr.next
            
        prev.next = curr.next
        curr.prev = prev
        self.count -= 1

        if (curr == self.head):
            self.head = curr.next
            curr.prev = None
        elif (curr == self.tail):
            prev.next = None
            self.tail = prev       

        return

    def delete(self, data) -> None:
        # Delete a node from the list who's value matches the supplied value
        current = self.head
        prev = self.head
        while current:
            if current.data == data:
                if current == self.tail:
                    prev.next = None
                    self.tail = prev
                elif current == self.head:
                    current.next.prev = None
                    self.head = current.next
                else:
                    prev.next = current.next
                    current.next = prev
                self.count -= 1
                return
            prev = current
            current = current.next

    def __getitem__(self, index):
        if index > self.count - 1:
            raise Exception("Index out of range.")
        current = self.head
        for n in range(index):
            current = current.next
        return current.data

    def __setitem__(self, index, value):
        if index > self.count - 1:
            raise Exception("Index out of range.")
        current = self.head
        for n in range(index):
            current = current.next
        current.data = value

    def __str__(self):
        myStr = ""
        for node in self.iter():
             myStr += str(node)+ " "
        return myStr

items = DoublyLinkedList()
items.addFirst("May")
items.add("the")
items.add("force")
items.add("be")
items.add("with")
items.add("you")
items.add("!")
print (items)

items.indexOf("with")
x = items.indexOf("you")
items.delete("you")
items.addAtIndex("us", x)
x = items.indexOf("!")
items.addAtIndex("all", x-1)
print(items)



