class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        binary_xor = (bin(x^y))
        binary_xor = binary_xor[2:]
        str_binary_xor = str(binary_xor)
    
        distance = str_binary_xor.count('1')
        
    
        return distance
        
        

        