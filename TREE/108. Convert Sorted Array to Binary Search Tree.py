from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST0(self, nums: List[int]) -> TreeNode:
        if nums == None:
            return None
        mid = len(nums)//2
        root = TreeNode(nums[mid])

        left = nums[:mid]
        right = nums[mid+1:]

        root.left = self.sortedArrayToBST(left)
        root.right = self.sortedArrayToBST(right)

        return root

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        self.sortedArrayToBST(nums,0,len(nums))

    def sortedArrayToBST(self,nums,left,right):
        if left == right:
            return None
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums,left,mid)
        root.right = self.sortedArrayToBST(nums,mid+1,right)
        return root
