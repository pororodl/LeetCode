import queue
class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self,root):
        if root ==None:
            return None
        q = queue.Queue()
        q.put(root)
        while not q.empty():
            cur = q.get()
            temp = cur.left
            cur.left = cur.right
            cur.right = temp
            if cur.left:
                q.put(cur.left)
            if cur.right:
                q.put(cur.right)
        return root


