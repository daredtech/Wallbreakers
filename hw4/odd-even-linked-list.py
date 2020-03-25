# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        
        if head:
            odd = head
            even = head.next
            odd_head = head
            even_head = even
            
            while even and even.next:
                
                odd.next = odd.next.next
                odd = odd.next
                
                even.next = even.next.next
                even = even.next
                
            odd.next = even_head
            
            return odd_head
        
        return head
                
                
                
        
       
        
        
        
        
                
        