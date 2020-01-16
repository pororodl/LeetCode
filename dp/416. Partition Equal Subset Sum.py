from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        w = sum(nums)

        if w % 2 == 1:
            return False
        w2 = w//2
        dp = [0]*(w2+1)
        for i in range(n):
            for j in range(w2,nums[i]-1,-1):
                dp[j]= max(dp[j],dp[j-nums[i]]+nums[i])
        if dp[w2]==w2:
            return True
        return False



    def Partition(self,nums) -> List[List]:
        n = len(nums)
        target2 = sum(nums)
        res = []
        if target2%2==1:
            return res
        target = target2//2
        record = [-1]*(target+1)    # 用一个record 记录第一次出现的
        dp = [False]*(target+1)
        dp[0]= True
        for i in range(target + 1):
            if nums[0] == i:
                dp[i] = True
                record[i]=0
        for i in range(1,n):
            j = target
            while j > nums[i]-1:
                dp[j] = dp[j] or dp[j-nums[i]]
                if record[j] == -1 and dp[j]==True:
                    record[j] = i
                j-=1
                if dp[target]==True:
                    break
        if dp[target]==False:
            return res

        print(record)

        res.append(nums[record[target]])
        while record[target] !=-1:
            target = target-nums[record[target]]
            if target <1:
                break
            res.append(nums[record[target]])
        return res

if __name__ == '__main__':
    nums = [1,4,6,8,7]
    nums = [1,2,3,4,5,6,7,8]
    s = Solution()
    print(s.Partition(nums))










