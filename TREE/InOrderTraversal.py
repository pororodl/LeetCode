class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def InOrderTraversal(self, root): # 左中右
        res = []
        self.iterative_inorder(root, res)
        return res

    def iterative_inorder(self, root, res):
        stack = []  # stack 中存的是TreeNode 结点对象
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            if stack:
                root = stack.pop()
                res.append(root.val)
                root = root.right
        return res


if __name__ == '__main__':
    s = Solution()
    l1 = TreeNode(1)
    l2 = TreeNode(2)
    l3 = TreeNode(3)
    l4 = TreeNode(4)
    l5 = TreeNode(5)
    l6 = TreeNode(6)
    l7 = TreeNode(7)

    root = l1
    l1.left = l2
    l1.right = l3
    l2.left = l4
    l2.right = l5
    l3.left = l6
    l3.right = l7

    print(s.InOrderTraversal(root))
