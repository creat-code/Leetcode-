# Last updated: 11/5/2026, 9:23:51 PM
class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums)
        nums.sort()

        for i in range(n - 1):
            if nums[i] != i + 1:
                return False

        return nums[n - 1] == n - 1