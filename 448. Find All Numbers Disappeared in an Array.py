class Solution:
    def findDisappearedNumbers(self, nums):
        '''

        :param nums: : List[int]
        :return:  -> List[int]
        '''
        l = len(nums)
        res = []
        if l ==0 or l ==1:
            return res
        ref =[]
        for i in range(1,l+1):
            ref.append(i)
        print(ref)
        for j in range(0,l):
            if nums[j]==ref[nums[j]-1]:
                ref[nums[j]-1]=0
            if ref[nums[j]-1]==0:
                continue
        for i in range(0,l):
            if ref[i]!=0:
                res.append(i+1)
        return res

if __name__ == '__main__':
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    s = Solution()
    print(s.findDisappearedNumbers(nums))