# Time Complexity: O(N)
# Space Complexity: O(1)
# Algo simply simulates the rules

class Solution:
    def myAtoi(self, s: str) -> int:
        # max and min int
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31 
        
        # pointer
        i = 0
        # update until digit
        while i < len(s) and s[i] == ' ': 
            i += 1
        
        # no digits in input, return 0
        if i == len(s): 
            return 0
        
        # if lead char is sign
        if s[i] in {'+','-'}:
            sign = 1 if s[i] == '+' else -1
            i += 1
        # else
        else:
            sign = 1
        
        # if no digits in input, return 0
        if i == len(s):
            return 0
        
        res = 0
        while i < len(s) and s[i].isdigit():
            digit = int(s[i])
            
            # boundary checking
            if res > MAX_INT//10:
                return MAX_INT if sign == 1 else MIN_INT
            
            elif res == MAX_INT//10:
                
                if sign == -1 and digit > 8:
                    return MIN_INT       
                
                elif sign == 1 and digit > 7:
                    return MAX_INT
                
            res = res*10+digit
            
            i += 1
        # return  
        return sign*res
