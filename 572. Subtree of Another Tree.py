class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        res = False

        if s!=None and t!=None:
            if s.val ==t.val:
                res = self.isSameStru(s,t)
            if res!=True:
                res = self.isSubtree(s.left,t)
            if res!=True:
                res = self.isSubtree(s.right,t)
        return res



    def isSameStru(self,s,t):
        if t==None:
            return True
        if s==None:
            return False
        if s.val!=t.val:
            return False
        return self.isSameStru(s.left,t.left) & self.isSameStru(s.right,t.right)


    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if t ==None and s==None:
            return True
        if s ==None or t ==None:
            return False
        if s.val == t.val:
            return self.isEqual(s,t) or self.isSubtree(s.left,t) or self.isSubtree(s.right,t)
        return self.isSubtree(s.left,t) or self.isSubtree(s.right,t)

    def isEqual(self,s,t):
        if t ==None and s==None:
            return True
        if s ==None or t ==None:
            return False
        if s.val == t.val:
            return self.isEqual(s.left,t.left) and self.isEqual(s.right,t.right)

        return False




