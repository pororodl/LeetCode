# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        def helper(node):
            if not node:
                return 0, 0
            taken_left, not_left = helper(node.left)
            print(taken_left,not_left)

            taken_right, not_right = helper(node.right)
            print(taken_right,not_right)
            taken = node.val + not_left + not_right
            not_taken = max(taken_left, not_left) + max(taken_right, not_right)
            return taken, not_taken

        a, b = helper(root)
        return max(a, b)

if __name__ == '__main__':
