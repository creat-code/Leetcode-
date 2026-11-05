# Last updated: 11/5/2026, 9:23:09 PM
class Solution:
    def createGrid(self, m: int, n: int) -> List[str]:
        return ['.' + '#' * (n - 1)] * (m - 1) + ['.' * n]


        