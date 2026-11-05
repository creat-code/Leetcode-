# Last updated: 11/5/2026, 9:25:13 PM
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while  True:
            try:
                nums.remove(val)
            except:
                break
                
    