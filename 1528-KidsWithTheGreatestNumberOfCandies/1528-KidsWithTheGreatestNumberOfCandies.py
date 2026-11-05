# Last updated: 11/5/2026, 9:24:22 PM
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        return  [bool(kid + extraCandies >= max(candies)) for kid in candies]
        