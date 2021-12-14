class Stack:
     def __init__ (self):
          self.stac = []
          self.top = None
     def push (self, data): #push onto stack
          self.stac.insert(0, data)
          self.top = data
     def pop (self): #pop off the top of stack
          if(len(self.stac) != 0):
               return self.stac.pop(0)
          else:
               return None
     def size (self):  #how many in the stack
          return len(self.stac)
     def isEmpty(self):
          if (len(self.stac) <= 0):
               return True
          else: 
               return False
     def peek(self): #if stack is not equal to none, return the top item in stack. 
          if (len(self.stac) != 0):
               return self.stac[0]
          else:
               return None
          
class Queue:
     def __init__ (self):
          self.kew = []
     def enqueue(self, data):  #add to queue
          self.kew.insert(0, data)
     def dequeue(self):  #remove from queue
          data = self.kew.pop()
          return data
     def size(self) -> int:
          return len(self.kew)
     def isEmpty (self):
          if(len(self.kew) <= 0): 
               return True
          else: 
               return False
     def peek(self):
          if(len(self.kew) > 0):
               return self.kew[-1]
          else:
               return None
          
def isPalindrome (data) :
     stac = Stack()
     kew = Queue()
     for sPeek in data:
          stac.push(sPeek)
          kew.enqueue(sPeek)
     while stac.isEmpty() == False: 
          sPeek = stac.peek()
          qPeek = kew.peek()
          if(sPeek == qPeek):
               stac.pop()
               kew.dequeue()
          else: 
               return False
     return True

print(isPalindrome('racecar'))
print(isPalindrome('noon'))
print(isPalindrome('python'))
print(isPalindrome('madam'))



#Test:
# myStack = Stack()
# myStack.push('p')
# myStack.push('y')
# myStack.push('t')
# myStack.push('h')
# myStack.push('o')
# myStack.push('n')

# print(myStack.size())
# print(myStack.peek())
# print(myStack.pop())

# myQueue = Queue()
# myQueue.enqueue('p')
# myQueue.enqueue('y')
# myQueue.enqueue('t')
# myQueue.enqueue('h')
# myQueue.enqueue('o')
# myQueue.enqueue('n')

# print(myQueue.size())
# print(myQueue.peek())
# print(myQueue.pop())