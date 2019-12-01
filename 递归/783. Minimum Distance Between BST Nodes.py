class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        if root == None:
            return 0
        anslist = []
        res = float('inf')
        def InOrder(root,anslist):
            if root ==None:
                return []
            InOrder(root.left,anslist)
            anslist.append(root.val)
            InOrder(root.right,anslist)

        InOrder(root,anslist)
        for i in range(len(anslist)-1):
            res = min(res,anslist[i+1]-anslist[i])
        return res
