# Last updated: 11/5/2026, 9:23:07 PM
class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        mn = min(nums1)
        count = sum(1 for x in nums1 if x % 2 == 1)

        return mn % 2 == 1 or count == 0
            

            

            

        