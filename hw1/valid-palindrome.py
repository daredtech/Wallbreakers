class Solution(object):
    def isPalindrome(self, some_string):
    
        if len(some_string) < 2:
            return True

        #ignore the case
        #ignore characters

        ignore_dict = [' ', '!', '#', ',', '.', ':', '@', '$', '&', '-', '--', '_', '?', '"', "'", '\\', ';', ')', '(', '}', '{', '`']

        pointer_b = 0
        pointer_e = len(some_string) - 1

        some_string = some_string.lower()


        while pointer_b < pointer_e:

            if some_string[pointer_b] in ignore_dict:
                pointer_b = pointer_b + 1
                continue

            if some_string[pointer_e] in ignore_dict:
                pointer_e = pointer_e - 1
                continue

            else:
              
                if some_string[pointer_b] == some_string[pointer_e]:
                    pointer_e = pointer_e - 1
                    pointer_b = pointer_b + 1
                    continue

                else:
                    return False

        return True 
