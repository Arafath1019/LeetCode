# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        
        pointer = head
        
        integer = 0
        
        temp = 0
        
        lst = []
        
        while pointer is not None:
            lst.append(pointer.val)
            pointer = pointer.next
        
        lst = lst[::-1]
        
        for element in lst:
            integer += (element * (2**temp))
            temp += 1
        
        return integer