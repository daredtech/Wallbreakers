class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        common = ""
        
        if len(strs) == 1:
            return strs[0]
        
        elif strs == []:
            return common
        
        shortest_word = min(strs, key = len)
        
        for index in range(0, len(shortest_word)):
            
            for word in strs:
                if word[index] == shortest_word[index]:
                    pass
                else:
                    return common
            common = common + word[index]
                
        return common
        