# Time Complexity: O(N)- one pass
# Space Complexity: O(1)- constant space
# Two pointer greedy approach

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Two pointer greedy approach
        
        l = 0
        r = len(height) - 1
        maxA = 0
        while l < r: 
            # calc and update local area
            w = r - l
            h = min(height[l], height[r])
            area = w*h
            maxA = max(area, maxA)
            # keep larger bar locally
            if height[r] >= height[l]:
                l += 1
            else:
                r -= 1
        return maxA
