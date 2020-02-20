class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        
        alphabet = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
       
        translated_words = []
        
        for word in words:
            translated_word = ''
            
            for character in word:
                translated_word = translated_word + alphabet[ord(character.lower())-97]
                
            translated_words.append(translated_word)
            
     
        unique = set(translated_words)
        
        return len(unique)
            
                
                
        
        
        