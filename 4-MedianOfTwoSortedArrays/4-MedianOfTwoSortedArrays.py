# Last updated: 11/5/2026, 9:25:29 PM
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        
        if len(nums1) % 2 == 1:
            return nums1[int(len(nums1)//2)]
        else:
            return (nums1[int(len(nums1)/2)] + nums1[int(len(nums1)/2  - 1)]) / 2
        