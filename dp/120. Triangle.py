class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        n = len(triangle[-1])
        if m==0 or n ==0:
            return 0

        if n==1:
            return triangle[-1][-1]


        dp = [[0 for i in range(n)] for j in range(m)]
        # 倒着更新，先更新最后一行
        for i in range(n):
            dp[m-1][i]=triangle[-1][i]

        for i in range(m-2,-1,-1):
            for j in range(0,i+1):
                dp[i][j]=min(dp[i+1][j],dp[i+1][j+1])+triangle[i][j]

        return dp[0][0]

