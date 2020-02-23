class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
      
        g.sort()
        s.sort()
        
        number_of_content_children = 0
        greed = 0
        
        for cookie_size in s:
            #if went through all the children
            if greed == len(g):
                break
            
            if cookie_size >= g[greed]:
                number_of_content_children += 1
                greed += 1           
                        
        return number_of_content_children
      
        
        