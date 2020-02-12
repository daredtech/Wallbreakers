class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) == 1:
            return True
        
        elif word[0].isupper():
            word = word[1:]
            
        return word.islower() or word.isupper()


        
        
#         if word.isupper() == True or word.islower() == True:
#             return True
        
#         else:
#             for index, character in enumerate(word):
#                 if index == 0:
#                     first_letter_upper = word[index].isupper()
                    
#                 else:
#                     if first_letter_upper == True and character.isupper() == True:
#                         return False
#                     elif first_letter_upper == False and character.isupper() == True:
#                         return False
            
#             return True
                    
                
            