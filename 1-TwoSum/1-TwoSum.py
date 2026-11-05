# Last updated: 11/5/2026, 9:25:32 PM
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    list1=[]
                    list1.append(i)
                    list1.append(j)
                    return list1