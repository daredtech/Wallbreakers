class Solution(object):
    def maxProfit(self, prices):
        
        if prices == []:
            return 0
        
        else:
            
            min_value = prices[0]
            current_profit = 0
            max_profit = 0
            
            for index in range(0, len(prices)):
                min_value = min(min_value, prices[index])
                current_profit = prices[index] - min_value
                max_profit = max(current_profit, max_profit)
                    
                    
        return(max_profit)
                
