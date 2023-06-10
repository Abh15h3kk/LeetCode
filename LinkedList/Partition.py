from LinkedList import LinkedList, Node

def partition(head,x):
    # Creating two dummy nodes and two tails
    left = Node()
    right = Node()
    ltail = left
    rtail = right
    # Iterating through LinkedList and adding elements to the left and right dummy node
    while head:
        if head.value < x:
            ltail.next = head
            ltail = ltail.next
        else:
            rtail.next = head
            rtail = rtail.next    
        head = head.next
    # Joining left and right LinkedList and pointing the right LinkedList to null
    ltail.next = right.next
    rtail.next = None

    return left.next

def partition2(head,x):
    

customLL = LinkedList()
customLL.generate(10,0,99)
print(customLL)
head = partition(customLL.head, 30)
while head:
    print(head.value)
    head = head.next
