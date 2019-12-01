# 有一群牛站成一排，每头牛都是面朝右的，每头牛可以看到他右边身高比他小的牛。
# 给出每头牛的身高，要求每头牛能看到的牛的总数。

class Solution:
    def cowSeeNum(self,nums):
        l = len(nums)
        res = 0
        if l<=1:
            return res
        stack = []
        nums.append(float('inf'))
        for i in range(l+1):
            while len(stack)!=0 and nums[i]>=nums[stack[-1]]:
                t = stack.pop()
                res += i-t-1

            stack.append(i)

        return res


if __name__ == '__main__':
    nums = [5,4,5,3,2]
    s = Solution()
    print(s.cowSeeNum(nums))

