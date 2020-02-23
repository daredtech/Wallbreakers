class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        
        nomination = {5:0, 10:0, 20:0}
        correct_change = False
        
        for bill in bills:
            nomination[bill] += 1
            
            if bill == 10:
                if nomination[5] >= 1:
                    nomination[5] = nomination[5] - 1
                else:
                    return correct_change
                      
            
            elif bill == 20:
                if nomination[10] >= 1 and nomination[5] >= 1:
                    nomination[5] = nomination[5] - 1
                    nomination[10] = nomination[10] - 1
                    
                elif nomination[5] >= 3:
                    nomination[5] = nomination[5] - 3
                
                else:
                    return correct_change
                
            
        correct_change = len(bills) > 0
                    
                
            
        return correct_change
       