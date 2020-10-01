# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        prev = None
        
        p = head
        
        while p is not None:
            future = p.next
            p.next = prev
            prev = p
            p = future
        
        head = prev
        
        return head
        