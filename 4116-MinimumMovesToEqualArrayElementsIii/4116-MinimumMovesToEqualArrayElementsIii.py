# Last updated: 11/8/2026, 5:15:25 PM
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        count = 0
        big = max(nums)
        for num in nums:
            count += big - num
        return count

        