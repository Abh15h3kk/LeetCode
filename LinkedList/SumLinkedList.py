from LinkedList import LinkedList, Node

def sumLinkedList(llA,llB):
    dummy = Node()
    cur = dummy

    carry = 0

    while llA or llB or carry: # carry here for edge case of single values like 5+8
        v1 = llA.value if llA else 0
        v2 = llB.value if llB else 0

        #new digit
        val = v1 + v2 + carry
        carry = val / 10
        val = val % 10
        cur.next = Node(val)

        #pointers
        llA = llA.next if llA else None
        llB = llB.next if llB else None
        cur = cur.next
    return dummy.next