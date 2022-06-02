# Time Complexity: O(log(N)) where N is input number
# Space Complexity: O(1) constant space

# Iterate through array and use simple math to reverse integer digit by digit:

class Solution:
    def reverse(self, x: int) -> int:
        # 1) sign
        # 2) dealing with the actual reversal
        # 3) dealing with overflow
        
        # 1)
        sign = 1 if x >= 0 else -1
        x = abs(x)
        #2) 
        # use math operations 
        
        # 3)
        #we don't have to consider the overflow case until rev >= maxint//10
        
        MAX_INT = 2**31 - 1
        rev = 0
        while x != 0:
            digit = x % 10
            x //= 10
            
            if rev > MAX_INT//10: 
                return 0
            
            if rev == MAX_INT:
                if x != 0: 
                    return 0
                elif sign == 1 and digit <= 7 or sign == -1 and digit <= 8:
                    return sign*(rev*10 + digit)
 
            rev = rev*10 + digit
        
        return sign*rev
