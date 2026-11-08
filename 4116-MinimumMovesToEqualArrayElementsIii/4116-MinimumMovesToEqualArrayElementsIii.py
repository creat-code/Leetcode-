# Last updated: 11/8/2026, 5:16:29 PM
class Solution:
    def minMoves(self, nums: List[int]) -> int:

        return sum(max(nums) - num for num in nums)

        