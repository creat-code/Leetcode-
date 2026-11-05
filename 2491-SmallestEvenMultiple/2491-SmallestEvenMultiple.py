# Last updated: 11/5/2026, 9:23:58 PM
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n % 2 == 0:
            return n
        return n*2
        