class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        my_dict = {}
        
        for num in nums:
            if num not in my_dict:
                my_dict[num] = 1
            else:
                my_dict[num] = my_dict[num] + 1
                
        for key in my_dict:
            if my_dict[key]!=2:
                return key
            
        print(my_values)
        print(my_keys)
            
        