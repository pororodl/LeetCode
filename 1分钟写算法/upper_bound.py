class Solution():
    def binary_search(self,nums,target):
        '''

        :param nums:
        :param target:
        :return:返回数组中target的下标，如果不存在target ,则返回数组长度
        '''
        low,high = 0,len(nums)-1
        while low<=high:
            mid = low+(high-low)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                high = mid-1
            else:
                low = mid+1
        return len(nums)

    def upper_bound(self, nums, target):
        '''
        :param nums: 升序的数组
        :param target:
        :return: 数组nums中比target大的第一个数字的下标,如果不存在，则返回数组长度
        '''
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] <= target:
                low = mid + 1
            else:
                high = mid - 1
        return low

    def lower_bound(self,nums,target):
        '''
        :param nums:
        :param target:
        :return:数组nums中大于等于target的第一个数字的下标,如果不存在，则返回数组长度
        '''
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] >= target:
                high = mid - 1
            else:
                low = mid+1
        return low


    # 最后一个小于等于target的数
    def last_min_euqal(self,nums,target):
        '''
        :param nums:
        :param target:
        :return:返回最后一个小于等于target的数，如果不存在，则返回数组长度 ===>第一个大于target的数字-1
        '''
        low,high = 0,len(nums)-1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] <= target:
                low = mid + 1
            else:
                high = mid - 1
        if low==0:
            return len(nums)
        return low-1


    # 最后一个小于target 的数字
    def last_min(self,nums,target):
        '''
        :param nums:
        :param target:
        :return:返回最后一个小于target 的数字，如果不存在返回数组的长度 ===>第一个大于等于target的数字的下标-1
        '''
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] >= target:
                high = mid - 1
            else:
                low = mid + 1
        if low==0:
            return len(nums)
        return low-1

if __name__ == '__main__':
    nums= [1,2,2,2,2,3,3,3]
    s= Solution()
    # print(s.binary_search(nums,60))
    # print(s.lower_bound(nums,2))
    # print(s.last_min(nums,0))
    print(s.last_min_euqal(nums,0))