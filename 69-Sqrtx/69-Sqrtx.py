# Last updated: 11/5/2026, 9:24:57 PM
class Solution:
    def mySqrt(self, x: int) -> int:
        i = 1
        while i*i < x:
            i += 1

        if i*i > x:
            return i-1
        return i