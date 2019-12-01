class Solution:
    def findDuplicates(self, nums):
        '''

        :param nums: : List[int]
        :return: -> List[int]
        '''
        l = len(nums)
        res = []
        if l ==0 or l ==1:
            return res
        nums.insert(0,0)
        for i in range(1,l+1):
            # 如果数字等于下标，就不管，进行下一次循环
            if nums[i]==i:
                continue
            # 如果数字不等于下标，就和以数字为下标的位置的数字进行比较，
                # 如果相等的话，就找到了重复的数字
                # 如果不相等的话，就和这个位置的数字交换
            else:
                while nums[i]!= i:
                    if nums[i] == nums[nums[i]]:
                        res.append(nums[i])
                        break

                    cur = nums[i]
                    nums[i]=nums[cur]
                    nums[cur]=cur

        return list(set(res))

if __name__ == '__main__':
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    s = Solution()
    print(s.findDuplicates(nums))