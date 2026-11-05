# Last updated: 11/5/2026, 9:24:38 PM
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        if n == 0 or n ==1:
            return True
        remainders = []
        while n >=1:
            remainders.append(n%2)
            n = n//2
        
        for i, x in enumerate(remainders):
            try:
                if (remainders[i] - remainders[i+1]) == 0:
                    return(False)
            except:
                if (remainders[-1] - remainders[-2]) == 0:
                    return(False)

        return(True)

                


        