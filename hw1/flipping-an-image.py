class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        if A == []:
            return []
        
        else:
            for row in A:
                
                if len(row) > 0:
                    row.reverse()
                  
                    
                    for index in range(0, len(row)):
                        if row[index] == 0:
                            row[index] = 1
                            
                        else:
                            row[index] = 0
                
        
        return A
        
        