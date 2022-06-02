# Runtime Complexity: O(N)
# Spacetime Complexity: O(26) ~ O(1)

# Two pointer method/one-pass linear solution
# 1) iterate through string with right pointer
# 2) add character at pointer to a hashmap if character isn't currently in the hashmap
# 3) if character at index is in hashmap, remove character at left pointer and increment left pointer
#    until seen character is removed.
# 4) update length varaible

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
