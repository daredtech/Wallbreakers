class Solution(object):
    def isIsomorphic(self, s, t):

        
        dict_s = {}
        dict_t = {}
        
        
        if len(s) != len(t):
            return False
        
        
        else:
            
            counter = 1
            for character in s:
                if character not in dict_s:
                    dict_s[character] = [counter]
                    
                else:
                    dict_s[character].append(counter)
                counter += 1
                
            print dict_s
                
            counter = 1 
            for character in t:
                if character not in dict_t:
                    dict_t[character] = [counter]

                else:
                    dict_t[character].append(counter)
                counter += 1
                
            print dict_t
            
            if sorted(dict_s.values()) == sorted(dict_t.values()):
                return True
            
            
            else:
                return False
            

        