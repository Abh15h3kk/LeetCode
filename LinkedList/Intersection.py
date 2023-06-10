from LinkedList import LinkedList, Node

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        llA = headA
        llB = headB
        while llA != llB:
            llA = llA.next if llA else headB
            llB = llB.next if llB else headA
        return llA

def length(ll):
    node = ll.head
    result = 0
    while node:
        result+=1
        node = node.next
    return result

def intersection(llA,llB):
    if llA.tail != llB.tail:
        return False

    lenA = len(llA)
    lenB = len(llB)

    shorter = llA if lenA < lenB else llB
    longer = llB if lenA < lenB else llA

    diff = len(longer) - len(shorter)
                                  
    shorternode = shorter.head
    longernode = longer.head

    for i in range(diff):
        longernode = longernode.next

    while shorternode is not longernode:
        shorternode = shorternode.next
        longernode = longernode.next
    
    return longernode


def addSameNode(llA, llB, value):
    tempNode = Node(value)
    llA.tail.next = tempNode
    llA.tail = tempNode
    llB.tail.next = tempNode
    llB.tail = tempNode

llA = LinkedList()
llA.generate(3,0, 10)

llB = LinkedList()
llB.generate(4,0, 10)

addSameNode(llA, llB, 11)
addSameNode(llA, llB, 14)

print(llA)
print(llB)

print(intersection(llA, llB))

