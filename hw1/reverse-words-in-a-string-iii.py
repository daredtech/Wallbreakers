class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        tokens = s.split()
        tokens_reversed = [token[::-1] for token in tokens]
       #print(tokens_reversed)
        reversed_string = ' '.join(tokens_reversed)
        #print(reversed_string)
        
        return reversed_string
        