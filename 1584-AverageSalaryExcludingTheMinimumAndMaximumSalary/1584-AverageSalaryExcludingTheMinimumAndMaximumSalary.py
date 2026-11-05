# Last updated: 11/5/2026, 9:24:18 PM
class Solution:
    def average(self, salary: List[int]) -> float:
        sum = 0
        big = small = salary[0]
        for i in range(len(salary)):
            sum += salary[i]
            if salary[i] > big:
                big = salary[i]
            elif salary[i] < small:
                small = salary[i]
            

        sum -= (big + small)

        avg = sum/(len(salary) - 2)
        return avg