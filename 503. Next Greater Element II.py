from typing import List
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        oriLen = len(nums)
        for i in range(oriLen):
            nums.append(nums[i])
        stack = []
        res = [-1]*len(nums)

        for i in range(len(nums)):
            while len(stack)!=0 and nums[i]>nums[stack[-1]]:
                t = stack.pop()
                res[t]=nums[i]
                if len(stack)==0:
                    break
            stack.append(i)
        return res[0:oriLen]

    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res = [0]*len(T)
        stack = []
        for i in range(len(T)):
            while len(stack)!=0 and T[i]>T[stack[-1]]:
                t = stack.pop()
                res[t]= i-t
            stack.append(i)
        return res

if __name__ == '__main__':
    nums = [73, 74, 75, 71, 69, 72, 76, 73]
    s= Solution()
    print(s.dailyTemperatures(nums))
