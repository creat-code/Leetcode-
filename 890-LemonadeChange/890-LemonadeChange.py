# Last updated: 11/12/2026, 8:23:55 PM
class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        collected = [0] * 3

        for bill in bills:
            if bill == 5:
                collected[0] += 1
            elif bill == 10:
                collected[1] += 1
                if not collected[0]:
                    return False
                collected[0] -= 1
            else:
                if collected[1]:
                    collected[1] -= 1
                    if collected[0]:
                        collected[0] -= 1
                    else:
                        return False
                elif collected[0] > 2:
                    collected[0] -= 3
                else:
                    return False
        return True
            
        