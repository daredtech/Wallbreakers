class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        
        binary_number = bin(N)
        
        str_binary_number = str(binary_number)
        adjusted_number = str_binary_number[2:]
        
        max_length = 0
        current_length = 0
        leading_one = None
        
        for index, number in enumerate(adjusted_number):
            if leading_one == None and int(number) == 1:
                leading_one = index
                
            elif leading_one != None and int(number) == 1:
                current_length = index - leading_one 
                max_length = max(max_length, current_length)
                leading_one = index
                
        return max_length
        
            