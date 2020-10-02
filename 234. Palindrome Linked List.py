# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        p = head 
        lst = []
        while p is not None:
            lst.append(p.val)
            p = p.next
            
        str1 = ""
        
        for element in lst:
            if element < 0:
                element = abs(element)
                print(element)
            str1 += str(element)
        
        lst2 = lst
        lst2.reverse()
        str2 = ""
        
        for element in lst2:
            if element < 0:
                element = abs(element)
                print(element)
            str2 += str(element)
        
        temp = 0
        if str1 == str2:
            for element in lst:
                if element < 0:
                    temp += 1
            if temp%2 == 0:  
                return True
        return False

