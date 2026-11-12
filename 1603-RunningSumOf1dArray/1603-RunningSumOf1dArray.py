# Last updated: 11/12/2026, 6:03:34 PM
class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        running = []
        for i in range(len(nums)):
            running.append(sum(nums[:i+1]))
        return running
        