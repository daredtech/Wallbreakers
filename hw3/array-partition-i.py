class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sorted_nums = sorted(nums)
        n = len(nums) // 2
        
        max_sum = 0
        
        for index in range(0,(len(sorted_nums)),2):
            max_sum = max_sum + sorted_nums[index]
                
        return max_sum
            