# Last updated: 11/12/2026, 1:47:16 AM
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        out = []
        n = 0

        def right(n):
            for i in range(len(matrix[0])):
                if matrix[n][i] is not None:
                    out.append(matrix[n][i])
                    matrix[n][i] = None
                    
        def down(n):
            for i in range(len(matrix)):
                if matrix[i][-n-1] is not None:
                    out.append(matrix[i][-n-1])
                    matrix[i][-n-1] = None
                    
        def left(n):
            for i in range(len(matrix[0]) - 1, -1, -1):
                if matrix[-n-1][i] is not None:
                    out.append(matrix[-n-1][i])
                    matrix[-n-1][i] = None
                    
        def up(n):
            for i in range(len(matrix)):
                if matrix[len(matrix)-i-1][n] is not None:
                    out.append(matrix[len(matrix)-i-1][n])
                    matrix[len(matrix)-i-1][n] = None

        while len(out) < len(matrix) * len(matrix[0]):
            right(n)
            down(n)
            left(n)
            up(n)
            n += 1

        return out
        

        

        