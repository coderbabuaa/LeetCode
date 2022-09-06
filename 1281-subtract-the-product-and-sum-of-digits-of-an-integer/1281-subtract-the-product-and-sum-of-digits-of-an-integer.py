from functools import reduce # Since Python 3, reduce() is moved to functools

class Solution:
    
    # Helper function for reduce()
    def product_nums(self,x1,x2):
        return x1*x2

    
    def subtractProductAndSum(self, n: int) -> int:
        digit_chars = list(str(n)) # Get all the characters from the number, after converting it to string
        digits = list(map(int,digit_chars)) # Getting the digits from number. First converting the chars back to int and then converting map object to list
        
        return reduce(self.product_nums,digits) - sum(digits) # Return the diff between product and sum of digits