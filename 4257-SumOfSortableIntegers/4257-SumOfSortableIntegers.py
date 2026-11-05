# Last updated: 11/5/2026, 9:23:11 PM
class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        result = 0
        n = len(nums)
        divisors = list({x for i in range(1, int(n**0.5) + 1) if n % i == 0 for x in (i, n // i)})
        goal = sorted(nums)
        
        for subsize in divisors:
            i = 0
            valid = True
            while i + subsize <= len(nums):
                sub = nums[i:i+subsize]
                target = goal[i:i+subsize]
                
                # Find the single point where the sorted order breaks
                drop_idx = 0
                for k in range(subsize - 1):
                    if sub[k] > sub[k + 1]:
                        drop_idx = k + 1
                        break
                
                # Reconstruct the array from the drop point and compare once
                if sub[drop_idx:] + sub[:drop_idx] != target:
                    valid = False
                    break
                    
                i += subsize
                
            if valid:
                result += subsize
                
        return result
                
            