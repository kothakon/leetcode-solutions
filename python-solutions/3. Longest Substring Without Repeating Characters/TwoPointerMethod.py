class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = set()
        maxLength = i = 0
        # start and end pointer- i and j respectively
        # iterate through string
        for j in range(len(s)):
            while s[j] in seen:
                # if s[j] is in hashmap,  remove elements starting
                # from left until s[j] is removed
                seen.remove(s[i])
                i += 1
            # add character to hashmap
            seen.add(s[j])
            # update length
            maxLength = max(maxLength, len(seen))
        return maxLength
