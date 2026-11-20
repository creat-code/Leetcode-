# Last updated: 11/20/2026, 9:02:05 PM
class Solution:
    def minimizeSum(self, nums: list[int]) -> int:
        return min(map(sub, nlargest(3, nums), reversed(nsmallest(3, nums))))  # change the 2 smallest, 1 of each, or the 2 largest