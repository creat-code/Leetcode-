# Last updated: 11/20/2026, 9:02:11 PM
class Solution:
    def numOfStrings(self, patterns: list[str], word: str) -> int:
        count = 0
        for pattern in patterns:
            if pattern in word:
                count += 1
        return count
        