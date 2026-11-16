# Last updated: 11/16/2026, 9:33:45 PM
class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            nxt = []
            for i in range(0, len(s), k):
                nxt.append(str(sum(int(c) for c in s[i:i + k])))
            s = "".join(nxt)
        return s