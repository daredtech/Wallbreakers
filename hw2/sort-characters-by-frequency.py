class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        my_dict = {}
        
        for ch in s:
            if ch not in my_dict:
                my_dict[ch] = 1
                
            else:
                my_dict[ch]  += 1
                
        result = ''
        
        while my_dict != {}:
            max_dict = max(my_dict.values())
        
            for key, value in my_dict.items():
                
                if value == max_dict:
                    result = result + key*value
                    del my_dict[key]
                
                
        return(result)
            
       
        