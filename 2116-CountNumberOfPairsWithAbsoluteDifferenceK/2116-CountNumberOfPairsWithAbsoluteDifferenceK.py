# Last updated: 11/12/2026, 6:10:22 PM
class Solution:
    def countKDifference(self, nums: list[int], k: int) -> int:
        c = 0
        for i in range(len(nums)-1):
            for j in range(i,len(nums)):
                if abs(nums[i]-nums[j]) == k:
                    c += 1
        return c
        