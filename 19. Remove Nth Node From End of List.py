# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        if head.next == None:
            return None
        
        first = head 
        second = head
        count = 1
        
        while  count <= n:
            second = second.next
            count = count + 1
        
        if second is None:
            head.val = head.next.val
            head.next = head.next.next
            return head
        
        while second.next is not None:
            first = first.next
            second = second.next
        
        first.next = first.next.next
        
        return head