# Last updated: 11/18/2026, 9:57:03 PM
class Solution:
    def minChanges(self, s: str) -> int:
        i = count = 0
        while i < len(s):
            if s[i+1] != s[i]:
                count += 1

            i += 2
        return count
            

        