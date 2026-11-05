# Last updated: 11/5/2026, 9:23:49 PM
class Solution(object):
    def countPairs(self, nums, target):
        count = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] < target:
                    count += 1
        return count

        