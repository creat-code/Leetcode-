# Last updated: 11/5/2026, 9:24:41 PM
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        for num in nums:
            if not num:
                nums.remove(num)
                nums.append(0)
        