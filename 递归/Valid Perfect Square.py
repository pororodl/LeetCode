class Solution:
    cunList = [0]*50000
    def numSquares(self, n: int) -> int:
        if int(n**0.5)**2 == n:
            return 1

        ansmin = float('inf')
        for i in range(1,n):
            if i**2>n:
                break
            if self.cunList[n-i**2]!=0:
                ansmin = min(ansmin,self.cunList[n-i**2])
            else:
                temp = self.numSquares(n-i**2)
                ansmin=min(ansmin,temp)
                self.cunList[n-i**2]=temp
        return ansmin+1

if __name__ == '__main__':
    s = Solution()
    print(s.numSquares(4**2+5**2+6**2))