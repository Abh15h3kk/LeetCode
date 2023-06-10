from LinkedList import LinkedList, Node

class Solution:
    def sortLinkedList(self,head):
        if head is None or head.next is None:
            return head
        
        left = head                 # initiated head as left element for left list
        right = self.getMid(head)   # right.next will be the left element of the right list
        tmp = right.next            # storing the left element of the right list in a temp variable
        right.next = None           # initialize last element of left list to None
        right = tmp

        left = self.sortLinkedList(left)
        right = self.sortLinkedList(right)
        return self.merge(left, right)


    def getMid(self,head):
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def merge(self,left,right):
        dummy = tail = Node()

        while left and right:
            if left.value < right.value:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next

        if left:
            tail.next = left
        if right:
            tail.next = right

        return dummy.next
        
    
customLL = LinkedList()
customLL.generate(4,0,20)
print(customLL)
ins = Solution()
head = ins.sortLinkedList(customLL.head)
while head:
    print(head.value)
    head = head.next