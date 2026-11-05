# Last updated: 11/5/2026, 9:23:44 PM
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        outarr = []
        for i, char in enumerate(words):
            if x in char:
                outarr.append(i)
        return outarr

        