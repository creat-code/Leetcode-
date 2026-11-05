# Last updated: 11/5/2026, 9:25:07 PM
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        if target > max(nums):
            return len(nums)
        while target > nums[i]:
            i += 1
        return i
                
            
        