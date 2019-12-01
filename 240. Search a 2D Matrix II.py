class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False
        if target > matrix[-1][-1]:
            return False
        i = 0
        j = n-1
        while i<m and j >-1:
            if target ==matrix[i][j]:
                return True
            elif target<matrix[i][j]:
                j-=1
            else:
                i+=1
        return False

    def searchMatrix2(self,matrix, target):
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False
        if target > matrix[-1][-1]:
            return False
        i = 0
        j = n - 1
        while i < m and j > -1:
            res = self.rowBinarySearch(matrix,i,0,j,target)
            if res<0:
                return False
            elif matrix[i][res]==target:
                return True
            else:
                j = res
            res = self.colBinarySearch(matrix,j,i,m-1,target)
            if res>m-1:
                return False
            elif matrix[res][j]==target:
                return True
            else:
                i=res
        return False

    def rowBinarySearch(self,matrix,index,left,right,target):

        start = left
        end = right
        while start <= end:
            mid = (start + end) // 2
            if matrix[index][mid] == target:
                return mid
            elif matrix[index][mid] < target:
                start = mid + 1
            else:
                end = mid - 1

        return end

    def colBinarySearch(self, matrix, index, left, right, target):

        start = left
        end = right
        while start <= end:
            mid = (start + end) // 2
            if matrix[mid][index] == target:
                return mid
            elif matrix[mid][index] < target:
                start = mid + 1
            else:
                end = mid - 1

        return start

if __name__ == '__main__':
    # matrix = [
    #     [1, 4, 7, 11, 15],
    #     [2, 5, 8, 12, 19],
    #     [3, 6, 9, 16, 22],
    #     [10, 13, 14, 17, 24],
    #     [18, 21, 23, 26, 30]
    # ]
    matrix = [[9]]
    s = Solution()

    # target =
    # print(s.rowBinarySearch(matrix,3,0,4,100))
    # print(s.colBinarySearch(matrix,0,0,4,19))
    print(s.searchMatrix2(matrix,9))