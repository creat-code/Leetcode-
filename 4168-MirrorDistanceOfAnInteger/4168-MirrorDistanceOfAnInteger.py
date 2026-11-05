# Last updated: 11/5/2026, 9:23:20 PM
class Solution:
    def mirrorDistance(self, n: int) -> int:
        return abs(n - int(str(n)[::-1]))