class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        res = [0]

        def digui(root):
            if root == None:
                return float('inf')
            left = digui(root.left)
            right = digui(root.right)

            if root.left and root.left.val == root.val:
                left_l = left+1
            else:
                left_l = 0
            if root.right and root.right.val == root.val:
                right_r = right+1
            else:
                right_r = 0

            res[0] = max(res[0],left_l+right_r)
            return max(left_l,right_r)
        digui(root)
        return res[0]







