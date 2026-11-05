# Last updated: 11/5/2026, 9:23:30 PM
class Solution:
    def processStr(self, s: str) -> str:
        
        result = ""

        for i in range(len(s)):
            if s[i] == "#":
                result += result
            elif s[i] == "%":
                result = result[::-1]
            elif s[i] == "*":
                result = result[:-1]
            else:
                result += s[i]
        return result