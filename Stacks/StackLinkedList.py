class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None
    
    def __str__(self):
        return str(self.value)
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next
    
    def __str__(self):
        values = [str(x.value) for x in self]
        return ' -> '.join(values)

class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()

    def __str__(self):
        values = [str(x.value) for x in self.LinkedList]
        return '\n'.join(values)
    
    def isEmpty(self):
        if self.LinkedList.head is None:
            return True
        else:
            return False
    
    def push(self, value):
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node
    
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            nodevalue = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            return nodevalue

    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            nodevalue = self.LinkedList.head.value
            return nodevalue
    
    def delete(self):
        self.LinkedList.head = None


customStack = Stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)

print(customStack)
print('----')
print(customStack.peek())
print('----')
print(customStack.pop())
print('----')
print(customStack.push(9))
print('----')
print(customStack)
print(customStack.isEmpty())
print('----')
print(customStack.delete())
print('----')
print(customStack.isEmpty())