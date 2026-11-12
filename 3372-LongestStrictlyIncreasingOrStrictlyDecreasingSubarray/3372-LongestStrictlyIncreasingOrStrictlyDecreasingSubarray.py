# Last updated: 11/12/2026, 4:35:33 PM
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        res = 1
        inclen = declen = maxlen = 1
        


        for i in range(len(nums)-1):
            if nums[i+1] > nums[i]:
                inclen += 1
                declen = 1
            elif nums[i+1] < nums[i]:
                declen += 1
                inclen = 1
            else:
                inclen = 1
                declen = 1
            res = max(res, max(inclen,declen))
        return res

