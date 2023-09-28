from LinkedList import LinkedList, Node

def middleLinkedList(head):
    slow = head
    fast = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow

customLL = LinkedList()
customLL.generate(4,0,20)
print(customLL)
print(middleLinkedList(customLL.head))

