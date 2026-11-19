# Last updated: 11/19/2026, 10:52:55 PM
class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:

        for i in range(len(nums)):
            a = max(nums[:i+1])
            b = min(nums[i:])
            score = a - b
            if score <= k:
                return i
        return -1
        