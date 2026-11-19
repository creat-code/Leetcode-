# Last updated: 11/19/2026, 10:55:06 PM
class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        for i in range(len(nums)):
            if max(nums[:i+1]) - min(nums[i:]) <= k:
                return i
        return -1
        