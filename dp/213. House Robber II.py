from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums)==1:
            return nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[1], dp[0])

        for i in range(2, len(nums)-1):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        res1 = dp[-1]
        print(res1)

        nums2 = nums[1:]
        dp[0] = nums2[0]
        dp[1] = max(nums2[1], dp[0])

        for i in range(2, len(nums2)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums2[i])
        res2 = dp[len(nums2)-1]
        print(res2)
        return max(res1,res2)







