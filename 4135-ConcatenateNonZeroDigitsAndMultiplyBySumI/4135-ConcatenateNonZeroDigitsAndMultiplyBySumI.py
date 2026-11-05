# Last updated: 11/5/2026, 9:23:21 PM
class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n < 1:
            return 0
        num2 = ""
        sum = 0
        for char in str(n):
            if char != "0":
                num2 += char
                sum += int(char)
        return int(num2) * sum