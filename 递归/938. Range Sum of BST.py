class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        anslist = []
        res = 0
        def inOrder(root,anslist):
            if root == None:
                return []
            inOrder(root.left,anslist)
            anslist.append(root.val)
            inOrder(root.right,anslist)

        inOrder(root,anslist)
        i = 0
        while i<len(anslist) and anslist[i]<=R:
            if anslist[i]>=L:
                res+=anslist[i]

            i+=1
        return res