from typing import List
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        iLen = len(intervals)
        if iLen ==0:
            return 0
        intervals.sort(key=lambda x:x[1])
        end = intervals[0][1]

        cnt = 1
        print(intervals)
        for i in range(1,iLen):
            if intervals[i][0]<end:
                continue
            else:
                cnt+=1
                end = intervals[i][1]
        print(iLen-cnt)
        return iLen-cnt


if __name__ == '__main__':
    s = Solution()
    s.eraseOverlapIntervals([[0,2],[1,3],[2,4],[3,5],[4,6]])