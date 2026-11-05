# Last updated: 11/5/2026, 9:23:48 PM
class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        opt = 0
        l = 0
        r = 0
        for i in moves:
            if i == "_":
                opt += 1
            elif i == "L":
                l += 1
            else:
                r += 1
        if l > r:
            return l + opt - r
        else:
            return r + opt - l

        
