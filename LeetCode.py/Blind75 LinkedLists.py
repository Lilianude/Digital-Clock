from typing import Optional

head = [1,2,3,4,5]

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def reverseList(self, head):
        
        prev, curr = None, head

        while curr:
           nxt = curr.next # point to the next item in the linked list
           curr.next = prev # reverse it
           prev = curr # assign current item to previous
           curr = nxt
        
            
        return prev
    
print(Solution().reverseList(head))