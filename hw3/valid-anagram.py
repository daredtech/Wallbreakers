class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        characters = {}
        
        if len(s) != len(t):
            return False
        
        for character in s:
            if character not in characters:
                characters[character] = 1
            else:
                characters[character] = characters[character] + 1
        print(characters)
                
        for character in t:
            if character not in characters:
                return False
            else:
                characters[character] = characters[character] - 1
                if characters[character] == 0:
                    del characters[character]
                    
                    
        return True
                
        