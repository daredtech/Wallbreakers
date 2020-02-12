class Solution(object):
    def plusOne(self, digits):
        
        if digits == []:
            return digits
        
        digits_plus_one = []
        
        
        digits.reverse()
        carry = 0
        
        for index, digit in enumerate(digits):
            if digit < 9 or digit+carry < 9:
                digits[index] = digits[index] + 1
                digits.reverse()
                return digits
            else:
                digits[index] = 0
                carry = 1

        if carry == 1:
            print("here")
            digits.append(1)
            digits.reverse()
            return digits
                
                    
     