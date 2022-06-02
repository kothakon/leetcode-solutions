# Runtime Complexity: O(N^3)
# Spacetime Complexity: O(1)
# A substring can be defined by a start index and an end index.
# Can create every pair of start and end indices creates, essentially creating every substring
# Also must validate each substring in linear time, hence N(start index)*N(end index)*N(validation) = O(N^3)
# Results in TLE

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # helper function to check if a string is palindrome
        # takes left and right indices as boundaries to check
        # return tuple of start and end indices and length of substring
        def isPal(l: int, r: int) -> tuple:
            start = l
            end = r
            while l <= r:
                if s[l] != s[r]:
                    return ((start,end),(0))
                l += 1
                r -= 1
            return ((start,end), (end - start + 1))
        
        maxLength = length = start = end = 0
        # create each substring with nested loops
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                bounds, length = isPal(i,j)
                left, right = bounds
                # update maxlength and bounds
                if length > maxLength:
                    start, end = left, right
                    maxLength = length
        return s[start:end+1]
