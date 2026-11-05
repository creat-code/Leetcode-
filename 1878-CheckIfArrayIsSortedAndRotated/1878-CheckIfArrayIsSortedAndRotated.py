# Last updated: 11/5/2026, 9:24:11 PM
class Solution:
    def check(self, nums: List[int]) -> bool:
        i = 0
        n = len(nums) - 1
        while i < n and  (nums[i+1] >= nums[i]):
            i += 1 
        print(i)
        if i < n and (nums[0] >= nums[-1]):
            i += 1
            while i < len(nums)-1 and  (nums[i+1] >= nums[i]):
                i += 1
            print(i)

        if i == n:
            return True
        return False

