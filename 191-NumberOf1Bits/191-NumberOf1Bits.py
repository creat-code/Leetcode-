# Last updated: 11/5/2026, 9:24:43 PM
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            if (n % 2) == 1:
                count += 1
            n = n//2
        return count