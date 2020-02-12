class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        #hashtable solution, extra memory
        if len(nums) < 2:
            return []
        
        complement_values = {}
        
        for index, value in enumerate(nums):
            if value in complement_values.keys():
                return [complement_values[value], index]
            complement_values[target-value] = index

        return []
            
            
            
    
            
        #intuitive solution, make sure to cover the case with the same integers
#         if len(nums) < 2:
#             return []
        
#         for index_outter, value_outter in enumerate(nums):
            
#             for index_inner, value_inner in enumerate(nums[(index_outter+1):]):
#                 if (value_inner + value_outter) == target:
#                     return [index_outter, (index_outter+index_inner+1)]
    
#         return []



        
        