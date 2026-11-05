# Last updated: 11/5/2026, 9:23:13 PM
class Solution:
    def minOperations(self, s: str) -> int:
        # Check if already sorted
        if list(s) == sorted(s):
            return 0
        
        n = len(s)
        if n == 2:
            return -1
        
        mn = min(s)
        mx = max(s)
        
        # 1 operation: can sort s[1:] if s[0] is already minimal,
        # or sort s[:-1] if s[-1] is already maximal
        if s[0] == mn or s[-1] == mx:
            return 1
        
        # 2 operations: if min is present anywhere except exclusively at index n-1,
        # or max is present anywhere except exclusively at index 0
        if mn in s[:-1] or mx in s[1:]:
            return 2
        
        # 3 operations: min is only at the last index AND max is only at the first index
        return 3