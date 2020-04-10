from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p = m-1
        q = n-1
        while p>-1 and q>-1:
            if nums1[p]>=nums2[q]:
                nums1[p+q+1] = nums1[p]
                p-=1
            else:
                nums1[p+q+1] = nums2[q]
                q-=1
        while q>-1:
            nums1[q]=nums2[q]
            q-=1

