from typing import List

class Solution:
    def onequickSort(self, nums, low, high):
        temp = nums[low]
        while low < high:
            while low < high and nums[high] >= temp:
                high -= 1
            nums[low] = nums[high]

            while low < high and nums[low] <= temp:
                low += 1
            nums[high] = nums[low]
        nums[low] = temp
        return low

    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        low = 0
        high = len(nums) - 1
        k = high - k + 1
        index = self.onequickSort(nums, low, high)
        if k == index:
            return nums[index]
        while index != k:
            if index < k:
                low = index + 1
            if index > k:
                high = index - 1
            index = self.onequickSort(nums, low, high)
        return nums[index]