from typing import List
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        l = len(nums)
        # if l<3:
        #     return max(nums)
        heap = []
        re ={}
        heap.append(nums[0])
        re[nums[0]]=True
        for i in range(l):
            if nums[i] in re.keys():
                continue
            if len(heap) <3:
                heap.append(nums[i])
                if nums[i]<heap[0]:

                    heap[0],heap[-1] = heap[-1],heap[0]
                re[nums[i]]=True

            elif nums[i]>heap[0]:
                re[nums[i]]=True
                del re[heap[0]]
                heap[0] = nums[i]
                if heap[1]<heap[0]:
                    heap[1],heap[0] = heap[0],heap[1]

                if heap[2]<heap[0]:
                    heap[2], heap[0] = heap[0], heap[2]
        print(heap)
        if len(heap)<3:
            return max(heap)

        return heap[0]








