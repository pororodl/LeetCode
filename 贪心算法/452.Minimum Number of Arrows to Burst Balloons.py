from typing import List
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        iLen = len(points)
        if iLen == 0:
            return 0
        points.sort(key=lambda x: x[1])
        end = points[0][1]

        cnt = 1
        print(points)
        for i in range(1, iLen):
            if points[i][0] < end:
                continue
            else:
                cnt += 1
                end = points[i][1]
        return cnt

if __name__ == '__main__':
    s = Solution()
    print(s.findMinArrowShots([[10,16], [2,8], [1,6], [7,12]]))