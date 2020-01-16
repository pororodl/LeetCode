from typing import List
class Solution:
    # 解题思路：对数组进行排序，计算每一个数字*出现该数字的次数和
    # 递归的子问题定义是：数字i之前的数字删除得到的积分最大的结果
    # 状态转移方程是：数字i之前的所有数字删除得到的最大积分有两种情况：1）删除数字i得到的积分和删除数字i-2之前的数字得到的积分
    #                                                           2） 删除数字i-1之前的数字得到积分
    # 取这两种情况下的最大值
    def deleteAndEarn(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        sortedNums = sorted(nums)

        s = [0]*(sortedNums[-1]+1)
        dp = [0]*(sortedNums[-1]+1)
        for e in sortedNums:
            s[e]+=e
        dp[0]=0
        dp[1]=s[1]
        for i in range(2,len(dp)):
            dp[i] = max(s[i]+dp[i-2],dp[i-1])
        return dp[-1]

