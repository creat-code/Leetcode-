# Last updated: 11/5/2026, 9:25:30 PM
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        current = []
        maxi = []
        for c in s:
            if c in current:
                idx = current.index(c)
                current = current[idx + 1:]
            current.append(c)
            print(current)
            maxi.append(len(current))
        return max(maxi)
        