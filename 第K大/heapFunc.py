from typing import List
import math
class Solution:

    def buildMaxHeap(self,arr):
        for i in range(math.floor(len(arr) / 2) - 1, -1, -1):
            self.heapify(arr, i)

    def heapify(self,arr, i):
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i
        if left < arrLen and arr[left] > arr[largest]:
            largest = left
        if right < arrLen and arr[right] > arr[largest]:
            largest = right
        if largest != i:
            self.swap(arr, i, largest)
            self.heapify(arr, largest)

    def swap(self,arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]


    def findKthLargest(self, nums: List[int], k: int) -> int:
        global arrLen
        arrLen = len(nums)
        self.buildMaxHeap(nums)
        for i in range(len(nums) - 1, len(nums) - k, -1):
            self.swap(nums, 0, i)
            arrLen -= 1  # 保证不和已经排好序的进行调整
            self.heapify(nums, 0)
        return nums[0]