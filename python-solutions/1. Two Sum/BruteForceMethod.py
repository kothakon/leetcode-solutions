# Runtime Complexity: O(N^2)
# Spacetime Complexity: O(1)
# Use nested for loops to compare every pairing of elements
# This method will result in TLE in other languages
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
