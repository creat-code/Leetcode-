# Last updated: 11/12/2026, 8:29:08 PM
class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        five=ten=0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                ten += 1
                if not five:
                    return False
                five -= 1
            else:
                if ten:
                    ten -= 1
                    if five:
                        five -= 1
                    else:
                        return False
                elif five > 2:
                    five -= 3
                else:
                    return False
        return True
            
        