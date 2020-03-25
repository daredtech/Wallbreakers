# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        storage = {}
     
        currentA = headA    
        while currentA:
            storage[currentA] = currentA.next
            currentA = currentA.next
            
        currentB = headB
        while currentB:
            if currentB in storage:
                if currentB.next == storage[currentB]:
                    return currentB
            currentB = currentB.next
            
        return currentB
            
        
        
