from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)   # n 行
        m = len(matrix[0])  # m 列
        recordi = False
        recordj = False
        for i in range(m):
            if matrix[0][i] == 0:
                recordi = True

                break
        for i in range(n):
            if matrix[i][0] == 0:
                recordj = True

                break
        print(recordi)
        print(recordj)
        for i in range(1,n):
            for j in range(1,m):
                if matrix[i][j]==0:
                    matrix[0][j]=0
                    matrix[i][0]=0
        print(matrix)
        for j in range(1,m):
            if matrix[0][j]==0:
                for i in range(1,n):
                    matrix[i][j]=0
        print(matrix)
        for i in range(1,n):
            if matrix[i][0]==0:
                for j in range(1,m):
                    matrix[i][j]=0

        if recordi == True:
            for i in range(m):
                matrix[0][i] = 0
        if recordj == True:
            for j in range(n):
                matrix[j][0]=0

if __name__ == '__main__':
    matrix =[
        [0, 1, 2, 0],
        [3, 4, 5, 2],
        [1, 3, 1, 5]
    ]
    s = Solution()
    s.setZeroes(matrix)
    print(matrix)
