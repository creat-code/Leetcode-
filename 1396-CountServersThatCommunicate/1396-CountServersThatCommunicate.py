# Last updated: 11/8/2026, 1:56:42 PM
class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        rows = [sum(row) for row in grid] 
        cols = [sum(col) for col in zip(*grid)]  

        ans = 0
        for i, row in enumerate(grid):
            for j, server in enumerate(row):
                if server and rows[i] + cols[j] > 2: 
                    ans += 1
        return ans