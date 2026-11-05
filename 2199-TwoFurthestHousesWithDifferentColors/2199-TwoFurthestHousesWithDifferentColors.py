# Last updated: 11/5/2026, 9:24:06 PM
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        for i in range(len(colors)):
            if colors[i] != colors[-1]:
                left = i
                break
        for i in range(len(colors)-1,-1,-1):
            if colors[i] != colors[0]:
                right = i
                break

        return max(len(colors)-1-left,right)

            
        