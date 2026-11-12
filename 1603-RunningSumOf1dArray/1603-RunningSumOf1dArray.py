# Last updated: 11/12/2026, 6:04:40 PM
class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        running = []
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            running.append(s)
        return running
        