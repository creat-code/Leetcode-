# Last updated: 11/14/2026, 12:09:52 AM
class Solution:
    def totalNumbers(self, digits):
        freq = [0] * 10
        for d in digits:
            freq[d] += 1

        count = 0

        for h in range(1, 10):
            if freq[h] == 0:
                continue
            freq[h] -= 1

            for t in range(0, 10):
                if freq[t] == 0:
                    continue
                freq[t] -= 1

                for u in range(0, 9, 2):
                    if freq[u] > 0:
                        count += 1

                freq[t] += 1

            freq[h] += 1

        return count