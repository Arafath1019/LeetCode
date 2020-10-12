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



# Solution-02

class Solution1:
    def middleNode(self, head: ListNode) -> ListNode:
        
        slow = head
        fast = head
        
        while(fast.next and fast.next.next):
            slow = slow.next
            fast = fast.next.next
        
        temp = head
        count = 0
        while(temp):
            count += 1
            temp = temp.next
        
        if(count%2==0):
            return slow.next
        else:
            return slow
        