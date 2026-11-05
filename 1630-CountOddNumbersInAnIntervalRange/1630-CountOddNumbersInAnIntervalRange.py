# Last updated: 11/5/2026, 9:24:14 PM
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high + 1) // 2 - (low // 2)