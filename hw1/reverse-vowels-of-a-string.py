class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        #s = "ai"
        
        vowels = ['a','e','u','o','i', 'A', 'E', 'U', 'O', 'I']
        start = 0
        end = len(s) - 1
        reversed_string = ''
        
        tokens = list(s)
        
        while start < end:
            if tokens[start] not in vowels:
                start += 1
                continue
            elif tokens[end] not in vowels:
                end -= 1
                continue
                
            tokens[start], tokens[end] = tokens[end], tokens[start]
            start += 1
            end -= 1
                    
                
        reversed_string = ''.join(tokens)
                
        return reversed_string
            