from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        s = sum(nums)
        target = s//2
        if s % 2 ==1:
            return False
        dp = [False]*(target+1)
        for i in range(target+1):
            if nums[0]==i:
                dp[i]=True
        for i in range(1,n):
            for j in range(target,nums[i]-1,-1):
                dp[j]=dp[j] or dp[j-nums[i]]
        return dp[target]



