# Last updated: 11/5/2026, 9:24:51 PM
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
       
        for i in range(0,n):
            nums1[m+i] = nums2[i]
        
        nums1.sort()

        
    
        
        