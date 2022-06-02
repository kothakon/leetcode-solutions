# Runtime Complexity: O(N) for loop
# Spacetime Complexity: O(N) for hashmap
# Keep a hashmap of seen elements.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # populate hashmap with seen elements along with their respective index.
        seen = {}
        for i in range(len(nums)):
            seen[nums[i]] = i
           
        # iterate through array and check if complement number exists in seen.
        for i in range(len(nums)):
            need = target - nums[i] 
            if need in seen:
                j = seen[need]
                # check that the matched numbers aren't identical
                if i != j:
                    return [i,j]
