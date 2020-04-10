class Solution:
    def generateMatrix(self, n: int): #-> List[List[int]]
        res = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            for j in range(n-i):
                res[i][j]=j
                res[j][i]=4*(n-2*i)-4-1

