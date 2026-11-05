# Last updated: 11/5/2026, 9:23:32 PM
class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            x = nums[i]
            s = 0
            while x > 0:
                s += x % 10
                x //= 10
            if s == i:
                return i
        return -1
        
        