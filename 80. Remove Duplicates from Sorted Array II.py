class Solution:
    def removeDuplicates(self, nums) -> int:
        '''

        :param nums: : List[int]
        :return:
        '''
        L = len(nums)
        if L<2:
            return len(nums)
        p = 0
        q = 0

        while q<L:
            if nums[p]==nums[q] and q-p+1>2:
                del nums[q]
                L -=1
            elif nums[p]==nums[q] and q-p+1<=2:
                q+=1
            else:
                p = q

        return L


