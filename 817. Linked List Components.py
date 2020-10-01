# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        temp = head
        lst = []
        G = set(G)
        li = 0
        while temp:
            if temp.val in G:
                lst.append([temp.val, li])
            temp = temp.next
            li += 1
            
            
        p = lst[0]
        c = 1
        for l in lst[1:]:
            if l[1] - p[1] != 1:
                c += 1
            p = l
        return c
        