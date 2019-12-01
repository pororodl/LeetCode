class Solution:
    def findErrorNums(self, nums):
        '''

        :param nums: : List[int]
        :return: -> List[int]
        '''
        l = len(nums)
        res = []
        ref = []
        for i in range(1, l + 1):
            ref.append(i)
        print(ref)
        for j in range(0, l):
            if nums[j] == ref[nums[j] - 1]:
                ref[nums[j] - 1] = 0
            elif ref[nums[j] - 1] == 0:
                res.append(nums[j])
                continue
        for i in range(0, l):
            if ref[i] != 0:
                res.append(i + 1)
        return res

if __name__ == '__main__':
    nums = [1, 2, 2, 4]
    s = Solution()
    print(s.findErrorNums(nums))