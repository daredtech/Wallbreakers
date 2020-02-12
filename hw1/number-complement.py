class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        #complement = None
        bin_number = bin(num)
        print(bin_number)
        
        bin_string = str(bin_number)
        complement = ''
        for index, number in enumerate(bin_string):
            if index < 2:
                continue
            else:
                print(number)
                if number == '1':
                    complement = complement + '0'
                else:
                    complement = complement + '1'
                    
        return (int(complement, 2))
         
      