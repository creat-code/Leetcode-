# Last updated: 11/20/2026, 9:01:57 PM
class Solution:
    def maxSelectedElements(self, nums: list[int]) -> int:
        dp = defaultdict(int)  
        for x in sorted(nums):
            dp[x + 1] = dp[x] + 1 
            dp[x] = dp[x - 1] + 1  
        return max(dp.values())
            

        