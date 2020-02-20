class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        set1 = set(nums1)
        set2 = set(nums2)
        

        intersection = []
        for number in set(nums1):
            if number in nums2:
                intersection.append(number)
                
        return set(intersection)