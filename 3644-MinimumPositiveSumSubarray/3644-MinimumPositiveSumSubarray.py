# Last updated: 11/14/2026, 4:00:01 PM
class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        minsum = float('inf')
        flag = 0
        for i in range(len((nums))):
            for j in range(l,r+1):
                subarray = nums[i:i+j]
                if len(subarray) >= l and len(subarray) <= r:
                    if sum(subarray) > 0:
                        flag = 1
                        minsum = min(minsum, sum(subarray))
        
        if not flag:
            return -1
        return minsum
        