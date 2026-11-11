# Last updated: 11/12/2026, 12:47:29 AM
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            return [0] * n

        if k < 0:
            i = (n + k) % n
            j = n - 1
        else:
            i = 1
            j = k

        total = sum(code[i : j + 1])

        ans = [0] * n
        for ind in range(n):
            ans[ind] = total
            total -= code[i]
            i = (i + 1) % n
            j = (j + 1) % n
            total += code[j]

        return ans