# Last updated: 11/5/2026, 9:23:56 PM
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        a = set(nums1)
        b = set(nums2)
        c = a.intersection(b)
        if a.isdisjoint(b):
            return -1
        for x in c:
            min = x
            break
        for x in c:
            if x < min:
                min = x
        return min

