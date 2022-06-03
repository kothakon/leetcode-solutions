# Time Complexity: O(N^2)
# Space Complexity: O(1) Constant space
# Brute Force method. Results in TLE

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Use two for loops to mark start and end of rectangle
        # Essentially check every valid rectangle
        maxA = area = 0
        for i in range(len(height)):
            for j in range(i+1,len(height)):
                area = (j-i)*min(height[j],height[i])
                maxA = max(maxA,area)
        return maxA
