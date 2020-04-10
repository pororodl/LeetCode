from typing import List
import queue
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid==None or len(grid)==0 or len(grid[0])==0 or grid[0][0]==1:
            return -1
        m = len(grid)
        n = len(grid[0])
        if grid[m-1][n-1]==1:
            return -1
        directions = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
        q = queue.Queue()
        q.put([0,0])
        res = 0
        while not q.empty():
            qLen = q.qsize()
            res+=1
            while qLen>0:
                cur = q.get()
                if cur[0]==m-1 and cur[1]==n-1:
                    return res
                grid[cur[0]][cur[1]]=1
                for e in directions:
                    x = cur[0]+e[0]
                    y = cur[1]+e[1]
                    if x<0 or x>=m or y<0 or y>=n or grid[x][y]==1 :
                        continue
                    q.put([x,y])
                qLen-=1
        return -1


if __name__ == '__main__':
    s = Solution()
    a = [[0,1],[1,0]]
    a2 =[[0,0,0],[0,1,0],[0,0,0]]
    parm= [[0,0,0],[1,1,0],[1,1,0]]

    print(s.shortestPathBinaryMatrix(parm))