# Last updated: 11/5/2026, 9:25:15 PM
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        while i<len(nums):
            if nums[i] == nums[i-1]:
                nums.pop(i)
            else:
                i += 1            



        