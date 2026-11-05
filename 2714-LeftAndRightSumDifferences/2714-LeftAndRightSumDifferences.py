# Last updated: 11/5/2026, 9:23:54 PM
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        lsum = [0]
        rsum = [0]
        diff = []
        i = 0
        while len(lsum) < len(nums):
            lsum.append(lsum[i] + nums[i])
            rsum.insert(0,nums[len(nums)-1-i] + rsum[len(rsum)-1-i])
            i += 1
        print(lsum,rsum)

        for i in range(len(nums)):
            diff.append(abs(lsum[i]-rsum[i]))

        return(diff)

        