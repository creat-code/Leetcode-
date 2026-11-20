# Last updated: 11/20/2026, 9:03:12 PM
class Solution:
    def maxArea(self, height: list[int]) -> int:
        l = 0
        r = len(height) - 1
        area = 0

        while l < r:  
            area = max(area, (r - l) * min(height[r],height[l]))

            if height[l] < height [r]:
                l += 1
            else:
                r -= 1

        return area
            
        