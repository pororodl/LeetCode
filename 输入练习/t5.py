from typing import List
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if not grid or grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        elif n <= 2:
            return n
        queue = [(0, 0, 1)]
        grid[0][0] = 1
        while queue:
            print(queue)
            i, j, step = queue.pop(0)
            for dx, dy in [(-1,-1), (1,0), (0,1), (-1,0), (0,-1), (1,1), (1,-1), (-1,1)]:
                if i+dx == n-1 and j+dy == n-1:
                    return step + 1
                if 0 <= i+dx < n and 0 <= j+dy < n and grid[i+dx][j+dy] == 0:
                    queue.append((i+dx, j+dy, step+1))
                    grid[i+dx][j+dy] = 1  # mark as visited
        return -1

if __name__ == '__main__':
    s = Solution()
    a = [[0,1],[1,0]]
    parm= [[0,0,0],[1,1,0],[1,1,0]]

    print(s.shortestPathBinaryMatrix(parm))