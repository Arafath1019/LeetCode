# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:   
    def mergeTwoLists(self, head1: ListNode, head2: ListNode) -> ListNode:
        
          if head1 == None:
            return head2
        
          elif head2 == None:
            return head1

          mergedHead = None;
            
          if head1.val <= head2.val:
            mergedHead = head1
            head1 = head1.next
            
          else:
            mergedHead = head2
            head2 = head2.next

          mergedTail = mergedHead

          while head1 != None and head2 != None:
            temp = None
            
            if head1.val <= head2.val:
              temp = head1
              head1 = head1.next
            
            else:
              temp = head2
              head2 = head2.next

            mergedTail.next = temp
            mergedTail = temp

          if head1 != None:
            mergedTail.next = head1
            
          elif head2 != None:
            mergedTail.next = head2

          return mergedHead


