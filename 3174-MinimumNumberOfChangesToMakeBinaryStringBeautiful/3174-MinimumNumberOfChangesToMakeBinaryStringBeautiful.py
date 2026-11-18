# Last updated: 11/18/2026, 9:59:05 PM
class Solution:
    def minChanges(self, s: str) -> int:
        count = 0
        """i = count = 0
        while i < len(s):
            if s[i+1] != s[i]:
                count += 1

            i += 2"""

        for i in range(0,len(s),2):
            if s[i+1] != s[i]:
                count += 1
        return count
            

        