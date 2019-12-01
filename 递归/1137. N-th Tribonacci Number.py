class Solution:
    def tribonacci(self, n: int) -> int:
        ansList = [0,1,1]
        for i in range(3,n):
            ansList.append(ansList[i-3]+ansList[i-2]+ansList[i-1])
        return ansList[n]
