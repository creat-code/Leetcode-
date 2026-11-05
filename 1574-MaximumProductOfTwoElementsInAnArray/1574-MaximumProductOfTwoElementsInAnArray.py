# Last updated: 11/5/2026, 9:24:20 PM
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        a = max(nums) - 1
        nums.remove(a + 1)
        b = max(nums) - 1
        return a * b

        