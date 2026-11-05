# Last updated: 11/5/2026, 9:24:46 PM
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        try:
            while nums[i] == nums[i+1]:
                i += 2
            return(nums[i])
        except:
            return(nums[i])

        