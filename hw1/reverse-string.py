class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        
        if len(s) < 2:
            return s
        
        front = 0
        end = len(s) - 1
        
        while front <= end:
            s[front], s[end] = s[end], s[front]
            front += 1
            end -= 1
            
        return s
     