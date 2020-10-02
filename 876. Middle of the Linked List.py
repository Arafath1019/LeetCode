# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        
        node = head
        
        temp = 0
        
        while node is not None:
            temp = temp + 1
            node = node.next
        
        if temp % 2 != 0:
            temp = ((temp-1)/2+1)
            node = head
            while temp > 1:
                node = node.next
                temp -= 1
            return node
        
        else:
            temp = ((temp/2)+1)
            node = head
            while temp > 1:
                node = node.next
                temp -= 1
            return node