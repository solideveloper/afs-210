class Stack:
     def __init__ (self):
          self.stac = []
          self.top = None
     def push (self, data):
          self.stac.insert(0, data)
          self.top = data
     def pop (self):
          if(len(self.stac) != 0):
               return self.stac.pop(0)
          else:
               return None
     def size (self):
          return len(self.stac)
     def isEmpty(self):
          if (len(self.stac) != 0):
               return False
          else: 
               return True
     def peek(self):
          if (len(self.stac) != 0):
               return self.stac[0]
          else:
               return None
          
class Queue:
     def __init__ (self):
          self.kew = []
     def enqueue(self, data):
          self.kew.insert(0, data)
     def dequeue(self):
          data = self.kew.pop()
          return data
     def size (self):
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
     while stac.isEmpty() != True: 
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