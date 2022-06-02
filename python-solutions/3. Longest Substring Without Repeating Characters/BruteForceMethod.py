# Runtime Complexity: O(N^3)
# Spacetime Complexity: O(26) ~ O(1)
# A substring can be defined by a start index and an end index.
# Can create every pair of start and end indices creates, essentially creating every substring
# Also must validate each substring in linear time, hence N(start index)*N(end index)*N(validation) = O(N^3)
# Results in TLE

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        maxLength = 0
        # outer two loops set start and end boundaries of substring
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                
                # create hashset to record seen letters
                seen = set()
                for k in range(i,j+1):
                    if s[k] in seen:
                        continue
                    seen.add(s[k])
                    
                #update max length
                maxLength = max(maxLength, len(seen))
                
        return maxLength
                    
