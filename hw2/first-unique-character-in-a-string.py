class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        my_dict = {}
        
        for index, item in enumerate(s):
            if item not in my_dict:
                my_dict[item] = index
                
            else:
                my_dict[item] = 'more'
                
        result = my_dict.values()
        print(result)
        
        result.sort()
        
        for item in result:
            if item != 'more':
                return item
            else:
                return -1
                
        return -1
        