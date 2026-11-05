# Last updated: 11/5/2026, 9:25:06 PM
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current = best = nums[0]
        for i in range(1,len(nums)):   
            current = max(nums[i], nums[i] + current)
            best = max(best, current)
        return best
        