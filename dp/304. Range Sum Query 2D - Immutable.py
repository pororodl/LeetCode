from typing import List
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m = len(matrix)
        if m == 0:
            self.res = [[0]]
        else:
            n = len(matrix[0])
            self.res = [[0 for i in range(n)] for j in range(m)]
            self.res[0][0] = matrix[0][0]
            for i in range(1,m):
                self.res[i][0] = self.res[i-1][0]+matrix[i][0]
            for j in range(1,n):
                self.res[0][j] = self.res[0][j-1]+matrix[0][j]

            for i in range(1, m):
                for j in range(1, n):
                    self.res[i][j] = self.res[i - 1][j] + self.res[i][j - 1] - self.res[i - 1][j - 1] + matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 ==0 and col1==0:
            return self.res[row2][col2]
        if row1==0:
            return self.res[row2][col2] - self.res[row2][col1-1]
        if col1 == 0:
            return self.res[row2][col2]-self.res[row1-1][col2]
        return self.res[row2][col2] + self.res[row1 - 1][col1 - 1] - self.res[row1 - 1][col2] - self.res[row2][
                col1 - 1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)