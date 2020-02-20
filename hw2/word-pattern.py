class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        word_bank = str.split()
        

        if len(word_bank) != len(pattern): 
            return False
        
        
        else:
            pattern_dict = {}
            str_dict = {}
            
            for index, item in enumerate(pattern):
                
                if item not in pattern_dict:
                    pattern_dict[item] = [index]
                    
                else:
                    pattern_dict[item].append(index)
                    
                    
            for index, item in enumerate(word_bank):

                if item not in str_dict:
                    str_dict[item] = [index]

                else:
                    str_dict[item].append(index)
                    
                    
            for key, value in str_dict.items():
                if value in pattern_dict.values():
                    del str_dict[key]
                    
                else:
                    return False
                
        if len(str_dict) == 0:
            return True
        
        else:
            return False
                    

            
            
                