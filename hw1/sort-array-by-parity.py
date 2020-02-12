class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        beg = 0
        end = len(A) - 1
        
        if len(A) < 2:
            return A
        
        else:
            
            while beg <= end:
                
                if A[beg] % 2 == 0:
                    beg += 1
                    
                else:
                    A[beg], A[end] = A[end], A[beg]
                    end -= 1
                     
        return A
                        