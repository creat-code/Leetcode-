# Last updated: 11/8/2026, 5:14:30 PM
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            count += max(nums) - num
        return count

        