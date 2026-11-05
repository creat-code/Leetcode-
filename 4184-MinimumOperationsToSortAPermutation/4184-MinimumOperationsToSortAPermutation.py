# Last updated: 11/5/2026, 9:23:18 PM
class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        drops_asc = 0
        drops_desc = 0
        min_val = nums[0]
        idx = 0
        
        for i in range(n):
            next_val = nums[(i + 1) % n]
            
            if nums[i] > next_val:
                drops_asc += 1
            if nums[i] < next_val:
                drops_desc += 1
                
            if nums[i] < min_val:
                min_val = nums[i]
                idx = i
                
        if drops_asc > 1 and drops_desc > 1:
            return -1
            
        ans = float('inf')
        
        if drops_asc <= 1:
            ans = min(ans, idx, n - idx + 2)
        if drops_desc <= 1:
            ans = min(ans, idx + 2, n - idx)
            
        return ans
        