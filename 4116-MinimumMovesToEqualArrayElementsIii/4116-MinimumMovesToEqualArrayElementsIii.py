# Last updated: 11/8/2026, 5:18:08 PM
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        big = max(nums)
        return len(nums) * big - sum(nums)

        