# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        for i in range(n):
            curr = curr.next

        if curr is None:
            return head.next  
        dummy = ListNode(0, head)        
        nth = dummy  
        while curr:
            nth = nth.next
            curr = curr.next 
        nth.next = nth.next.next 
        return dummy.next