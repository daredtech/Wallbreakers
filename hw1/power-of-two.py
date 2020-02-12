class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
         
        if n < 1:
            return False
        elif n == 1:
            return True
        
        else:
            
            div_number = n
            
            while div_number > 0:
                print(div_number)
                print(div_number % 2)
                
                if div_number == 2:
                    return True
                elif div_number % 2 == 0:
                    div_number = div_number / 2
                    
                else:
                    return False
                
        return True
                