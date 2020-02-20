class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        
        candy_options = set(candies)
        max_variety = min(len(candy_options), len(candies)/2)
        
        return max_variety
        
#         candy_options = {}
#         max_variety = len(candies)/2
        
#         for candy in candies:
#             if candy not in candy_options:
#                 candy_options[candy] = 1
#             else:
#                 candy_options[candy] += 1
                
#         return min(max_variety, len(candy_options.keys()))


        
        