def palindromeLinkedList(head):
    slow = head
    fast = head

    #Finding middle node
    while head and head.next:
        head = head.next.next
        slow = slow.next
    
    prev = None
    cur = slow
    #Reversing second half of the Linked List
    while cur:
        temp = cur.next
        cur.next = prev
        prev = cur
        cur.next = temp
    
    left = head
    right = prev
    while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next
    return True