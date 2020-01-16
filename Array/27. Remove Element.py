from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = len(nums)-1
        if i == j:
            if nums[i]==val:
                return 0
            else:
                return 1
        while i<j:
            while i<len(nums) and nums[i]!= val:
                i+=1
            while j >-1 and nums[j]==val:
                j-=1
            if i <j:
                nums[i]=nums[j]
                i+=1
                j-=1
        if nums[i]==val: # [2,2,3] val =2
            return i
        if j ==-1:    # [2,2] val =2
            return 0
        return j+1
if __name__ == '__main__':
    s = Solution()
    # nums = [3,2,2,3]
    nums =[2,2]
    print(s.removeElement(nums,2))



