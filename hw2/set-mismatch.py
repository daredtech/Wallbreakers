class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        my_nums = {}
        n = len(nums)
        nums.sort()
        
    
        for num in nums:
            
            if num not in my_nums:
                my_nums[num] = 1
             
            else:
                repeated = num
                my_nums[num] = 1
            
        
        for i in range(1, 10000):
            if i not in my_nums:
                return [repeated, i]
            
            