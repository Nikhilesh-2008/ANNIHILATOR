class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        m=len(matrix)
        n=len(matrix[0])
        r=[1]*m
        c=[1]*n
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    r[i]=0
                    c[j]=0
        for i in range(m):
            for j in range(n):
                if r[i]==0 or c[j]==0:
                    matrix[i][j]=0