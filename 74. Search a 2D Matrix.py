class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        '''

        :param matrix: : List[List[int]]
        :param target:
        :return:
        '''
        m = len(matrix)
        if m==0:
            return False
        n = len(matrix[0])
        if n ==0:
            return False
        if target>matrix[-1][-1]:
            return False
        start = 0
        end = m-1
        while start<=end:
            mid = (start+end)//2
            if matrix[mid][-1]==target:
                return True
            elif matrix[mid][-1]<target:
                start = mid+1
            else:
                end = mid-1
        print(start,end)
        row = start
        start = 0
        end = n - 1
        while start <= end:
            mid = (start + end) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                start = mid + 1
            else:
                end = mid - 1

        return False


    def binarySearch(self,List,target):
        l = len(List)
        start = 0
        end = l-1
        while start<=end:
            mid = int((end+start)/2)
            if List[mid]==target:
                return True
            elif List[mid]<target:
                start = mid+1
            else:
                end = mid-1
        # print('start,end',start,end)
        # return start
        if start>=l or end<=0:
            return False

        if List[end]==target:
            return True
        elif List[start]==target:
            return True
        else:
            return False

if __name__ == '__main__':
    # List = [1,2,3,6,7]
    # target = 2
    # matrix = [
    #     [1, 3, 5, 7],
    #     [10, 11, 16, 20],
    #     [23, 30, 34, 50]
    # ]

    # matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
    # matrix = [[1],[3]]
    matrix = [[1,1]]
    target = 1
    s = Solution()

    # print(s.binarySearch(List,target))
    print(s.searchMatrix(matrix,target))