from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pLen = len(prices)
        dp=[[0] for _ in range(2) for _ in range(pLen)]
        for i in range(pLen):
            if i-1 ==-1:
                dp[i][0]=0
                dp[i][1]=-float('inf')
                continue
            dp[i][0]= max(dp[i-1][0],dp[i-1][1]+prices[i])
            dp[i][1]=max(dp[i-1][1],-prices[i])
        return dp[pLen-1][0]



