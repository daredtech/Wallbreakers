class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        
        if A == []:
            return []
        
        old_row_length = len(A)
        old_col_length = len(A[0])
        
        new_matrix = []
        new_row_length = old_col_length
        new_col_length = old_row_length
        
        for row_index in range(0, new_row_length):
            new_row = []
            for col_index in range(0, new_col_length):
                new_row.append(0)
            new_matrix.append(new_row)
            
        print(new_matrix)
        
        
        
        for row_index in range(0, old_row_length):
            for col_index in range(0, old_col_length):
                
                new_matrix[col_index][row_index]= A[row_index][col_index] 
                        
                
        return new_matrix