class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        column_number = 0
        
        for index, value in enumerate(s):
            true_value = ord(value) - 64
            
            if len(s) == 1:
                return true_value
            else:
                column_number = 26 * column_number + true_value 
            
        return column_number
        
        
        