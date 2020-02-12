class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """

        
        self_dividing_nums = []
      
        for item in range(left, right+1):
            
            if item == 0:
                continue
            
            elif item / 10 > 0:
               
                modified_item = item
                
                while True:
                    
                    if modified_item > 9:
                        last_digit = modified_item % 10

                        if last_digit == 0:
                            break
                        else:
                            if item % last_digit != 0:
                                break
                            else:
                                modified_item = modified_item // 10
                              
                    else:
                        if item % modified_item != 0:
                            break
                        else:
                            self_dividing_nums.append(item)
                            break
                            
            else:
                self_dividing_nums.append(item)
    
                
        return self_dividing_nums
            
            
            
        