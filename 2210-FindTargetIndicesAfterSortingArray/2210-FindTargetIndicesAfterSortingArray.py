# Last updated: 11/5/2026, 9:24:04 PM
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        return list(range(sum(x < target for x in nums), sum(x <= target for x in nums)))