class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root, sum: int) -> bool:
        '''

        :param root: : TreeNode
        :param sum:
        :return:
        '''
        if root == None :
            return False
        if root.left == None and root.right ==None:
            return root.val==sum
        return self.hashPathSum(root.left,sum-root.val) or self.hasPathSum(root.right,sum-root.val)