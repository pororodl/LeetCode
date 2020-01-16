from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = j =0
        # temp = nums[0]
        while i<len(nums) and j < len(nums):
            j+=1
            if j<len(nums) and nums[j]>nums[i]:
                i+=1
                nums[i]=nums[j]

        return i+1
if __name__ == '__main__':
    s = Solution()
    nums = [0,0,1,1,1,2,2,3,3,4]
    s.removeDuplicates(nums)

