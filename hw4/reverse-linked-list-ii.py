# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
        def reverseBetween(self, head, m, n):
            if m == n:
                return head
            
            dummy_node = ListNode('Start')
            dummy_node.next = head
            value_before_m = dummy_node
            
            #safe the value before m
            for i in range(m - 1):
                value_before_m = value_before_m.next
                
            previous = None
            current = value_before_m.next
            
            #reverse sublist
            for i in range(n - m + 1):
                temp = current.next
                current.next = previous
                previous = current
                current = temp
                i += 1
            
            value_before_m.next.next = current            
            value_before_m.next = previous

            return dummy_node.next