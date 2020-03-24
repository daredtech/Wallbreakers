class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """

        stack_s = []
        stack_t = []
        
        for item in S:
            if item != '#':
                stack_s.append(item)
                
            elif item == '#' and stack_s != []:
                stack_s.pop()
        
        
        for item in T:
            if item != '#':
                stack_t.append(item)
                
            elif item == '#' and stack_t != []:
                stack_t.pop()
            
        
        return stack_t == stack_s
                
                
            