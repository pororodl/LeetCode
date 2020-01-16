class Solution:
    def nextGreaterElement(self, n: int) -> int:
        m = n
        if n //10<1:
            return n

        nList=[]
        while n>0:
            nList.append(n%10)
            n = n//10
        nList.reverse()
        self.nextPermutation(nList)
        res = 0
        for i in range(len(nList)):
            res += nList[i]*(10**(len(nList)-i-1))
        if res>0x7FFFFFFF or res<=m:
            return -1

        return res


    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 从后往前找到破坏升序的第一个数字
        # 然后从这个数字A往后找到最后一个大于它的数字B ，交换这两个数字
        # 反转这个数字B后面的所有数字
        if len(nums) == 2:
            self.reverse(nums,0, len(nums)-1)
        if len(nums) >= 3:
            i = len(nums)-2
            while i!= -1:
                if nums[i]<nums[i+1]:
                    break
                i-=1
            if i == -1:  # 从右往左全部都是升序的话，直接反转
                self.reverse(nums, 0, len(nums) - 1)

            else:
                j = i+1
                while j<len(nums):        # j 是后面部分第一个小于等于i 的数字，所有j-1 才是大于i 的最后一个数字，交换的时候要注意
                    if nums[j]<=nums[i]:
                        break
                    j+=1
                temp = nums[j-1]
                nums[j-1] = nums[i]
                nums[i] = temp
                # print(nums)

                self.reverse(nums, i + 1, len(nums) - 1)

    def reverse(self, nums, i, j):  # 包括i，包括j
            # print(nums)
            n = (j - i + 1) // 2
            for k in range(n):
                temp = nums[i + k]
                nums[i + k] = nums[j - k]
                nums[j - k] = temp

if __name__ == '__main__':
    s = Solution()
    n = 1999999999
    print(s.nextGreaterElement(n))
