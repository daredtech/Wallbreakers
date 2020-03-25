class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) == 0:
            return True
        
        elif len(s) % 2 !=0:
            return False
            
        my_stack = []
        
        for character in s:
            if character == '(':
                my_stack.append(')')
            elif character == '{':
                my_stack.append('}')
            elif character == '[':
                my_stack.append(']')
                
            else:
                if my_stack == []:
                    return False
                elif character != my_stack.pop():
                    return False
           
        #print(my_stack)
        if my_stack == []:
            return True
                
        return False
                
                
        