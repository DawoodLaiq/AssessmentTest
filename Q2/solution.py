# Definition for singly-linked list.

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
        #print(head.val)
        
        val, length = head, 0
        while val:
            val=val.next
            length+=1
        if length == n:
            return head.next
        val = head
        for i in range(1, length - n):
            val = val.next
        val.next = val.next.next
        
        return head
    #val=ListNode(0)
    #otal=val
    #total.next = ListNode(1)

    print(removeNthFromEnd([1,2,3,4,5],2))