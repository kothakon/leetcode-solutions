# Runtime Complexity: O(N) for loop
# Spacetime Complexity: O(N) for hashmap
# populate a hashmap with seen elements and check for pairs in one loop

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}
        # iterate through array
        for i in range(len(nums)):
            # number needed to add up to target
            need = target - nums[i] 
            if need in seen:
                return [i, seen[need]]
            # adds seen element to hashmap
            seen[nums[i]] = i
