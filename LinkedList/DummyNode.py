from LinkedList import LinkedList, Node

def add2(ll:Node):
    dummy = tail = Node()
    node = ll.head
    while node:
        tail.next = Node(node.value * 2)
        tail = tail.next
        node = node.next
    current = dummy.next
    while current is not None:
        print(current.value)
        current = current.next

customll = LinkedList()
customll.generate(5,0,10)
print(customll)
print(add2(customll))

