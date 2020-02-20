class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        from collections import Counter
        
        c_s = Counter(s)
        c_t = Counter(t)
        
        c_t.subtract(c_s)
        
        for letter in c_t:
            if c_t[letter] == 1:
                return letter
        
        return ''
        

            
                