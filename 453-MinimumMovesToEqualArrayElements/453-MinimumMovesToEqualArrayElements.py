# Last updated: 11/5/2026, 9:24:39 PM
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums) - len(nums) * min(nums)