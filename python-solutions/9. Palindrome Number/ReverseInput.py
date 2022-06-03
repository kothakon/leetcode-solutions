# Time Complexity: O(log(N)) where N is input integer. Only need to iterate through input's digits
# Space Complexity: O(1) Constant space

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # negative input case
        if x < 0:
            return False
        
        # make copy to maintain input
        y = x
        
        # rev number
        rev = 0
        while y != 0:
            digit = y % 10 
            y //= 10
            rev = rev * 10 + digit
            
        # check if reversed number equals input
        return rev == x
