class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        
        list_a = A.split()
        list_b = B.split()
        
        uncommon = []
        common = {}
        
        for word in list_a:
            if word not in common:
                common[word] = 1    
            else:
                common[word] = common[word] + 1
                
        for word in list_b:
            if word not in common:
                common[word] = 1    
            else:
                common[word] = common[word] + 1
                
        #uncommon = [word for word in common if common[word] == 1]
                
        for key, value in common.items():
            if value > 1:
                del common[key]
                
        for key, value in common.items():
            uncommon.append(key)
            
        return uncommon
                
        
        
        