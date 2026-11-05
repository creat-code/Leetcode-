# Last updated: 11/5/2026, 9:23:35 PM
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        st = set(word)
        count = 0

        for ch in st:
            if ch.isupper() and ch.lower() in st:
                count += 1

        return count
        