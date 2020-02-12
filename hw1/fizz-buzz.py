class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        fizz_buzz_list = []
        
        for number in range(1, n+1):
            
            if number % 5 == 0 and number % 3 == 0:
                fizz_buzz_list.append("FizzBuzz")
                
            elif number % 3 == 0:
                fizz_buzz_list.append("Fizz")
                
            elif number % 5 == 0:
                fizz_buzz_list.append("Buzz")
                
            else:
                fizz_buzz_list.append(str(number))
                
        return fizz_buzz_list
                
        