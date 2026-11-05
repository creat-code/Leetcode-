# Last updated: 11/5/2026, 9:25:00 PM
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits:
            return [1]

        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        return self.plusOne(digits[:-1]) + [0]
            
            
        