class Stack:
    def __init__(self,maxsize):
        self.maxsize = maxsize
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)
    
    def isEmpty(self):
        if self.list ==[]:
            return True
        else:
            return False
    
    def isFull(self):
        if len(self.list) == self.maxsize:
            return True
        else:
            return False
    
    def push(self,value):
        if self.isFull():
            return "The Stack is full"
        else:
            self.list.append(value)
    
    def pop(self):
        if self.isEmpty():
            return "The Stack is empty"
        else:
            return self.list.pop()
        
    def peek(self):
        if self.isEmpty():
            return "The Stack is empty"
        else:
            return self.list[-1]
        
    def delete(self):
        self.list = None


customStack = Stack(5)
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(4)
customStack.push(5)

print(customStack.isFull())
print('----')
print(customStack.isEmpty())
print('----')
print(customStack.peek())
print('----')
print(customStack.pop())
print('----')
print(customStack.isFull())
print('----')
print(customStack)
