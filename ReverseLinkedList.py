def reverseList(head):
        prev = None
        cur = head

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev