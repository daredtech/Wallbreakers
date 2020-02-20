class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        p = ''
        for ch in paragraph:
            if ch in punctuations:
                p = p + ' '
                
            else:
                p = p + ch
                
        
        print(p)    
        
        list_paragraph = p.lower().split()
        print(list_paragraph)
        
        my_dict = {}
        
        
        
        for word in list_paragraph:
            if word not in banned:
                #print(word)
                
                if word not in my_dict.keys():
                    my_dict[word] = 1
                    
                else:
                    my_dict[word] += 1
                    
        if len(my_dict) > 0:
            most_common = max(my_dict.values())
            for key, value in my_dict.items():
                if value == most_common:
                    return key