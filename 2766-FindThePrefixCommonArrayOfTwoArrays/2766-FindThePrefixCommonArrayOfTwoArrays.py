# Last updated: 11/5/2026, 9:23:53 PM
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        common = [0] * len(A)
        
        for i in range(len(A)):
            for j in range(len(A[:i+1])):
                if A[j] in B[:i+1]:
                    common[i] += 1
        return common
            


        