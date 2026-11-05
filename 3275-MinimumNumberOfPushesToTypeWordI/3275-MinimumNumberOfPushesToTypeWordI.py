# Last updated: 11/5/2026, 9:23:43 PM
class Solution:
    def minimumPushes(self, word: str) -> int:

        pushes = 0

        for i in range(len(word)):

            pushes += (i // 8) + 1

        return pushes