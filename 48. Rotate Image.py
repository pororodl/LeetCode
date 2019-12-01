class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        if n>1:
            for i in range(n//2):
                for j in range(n-1-2*i):
                    # temp = matrix[i][i+j]
                    # matrix[i][i+j] = matrix[i+j][n-i-1]
                    # matrix[i+j][n-i-1] = matrix[n-i-1][n-i-1-j]
                    # matrix[n - i - 1][n - i - 1 - j] = matrix[n-i-1-j][i]
                    # matrix[n-i-1-j][i] = temp


                    temp = matrix[n-i-1-j][i]
                    matrix[n - i - 1 - j][i] = matrix[n - i - 1][n - i - 1 - j]
                    matrix[n - i - 1][n - i - 1 - j] = matrix[i+j][n-i-1]
                    matrix[i + j][n - i - 1] = matrix[i][i+j]
                    matrix[i][i + j] = temp





if __name__ == '__main__':
    matrix = [
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16]
    ]
    s = Solution()
    s.rotate(matrix)
    print(matrix)

