# Last updated: 11/5/2026, 9:24:26 PM
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        x = hour + minutes / 60
        diff = (11 * x) % 12
        return min(diff, 12 - diff) * 30