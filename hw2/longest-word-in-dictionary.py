class Solution(object):
    def longestWord(self, words):
        
        #SHOULD DO WITH TRIE
  

        
# #         #words = ["d","do","dog","p","pe","pen","peng","pengu","pengui","penguin","e","el","ele","elep","eleph","elepha","elephan","elephant"]
        
#         my_collection = {}
#         max_word = ''
        
#         for word in words:
#             check = ''
            
#             # print('!!!', my_collection)  
            
#             for character in word:
#                 check = check + character
                
#                 if check in my_collection:
#                     continue
#                 else:
                    
#                     try:
#                         del my_collection[check[0:len(check)-1]]
#                         #my_collection[check] = 1
#                     except:
#                         pass
#                     my_collection[check] = 1
           
#         # print()
#         print(my_collection)   
        
#         if len(my_collection) != 0:
#             max_len = len(max(my_collection.keys()))
#             print(max_len)
            
#             for key, value in my_collection.items():
#                 if len(key) < max_len:
#                     del my_collection[key]
                    
                    
#             my_collection.keys(sort)
#             print()
                    
           
#             return(min(my_collection.keys()))
                
        
#         else:
#             return ''

            
 