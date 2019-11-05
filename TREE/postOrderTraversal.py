class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def postOrderTraversal(self, root: TreeNode):
        # 后序遍历（左右中）反过来是中右左，和前序遍历的差别就是左和右的差别，如果在前序遍历的代码中把左和右的结果调换，再把最后得到的结果反向就可以得到后序遍历的结果了
        res = []
        stack = []
        # while stack or root:
        #     if root:
        #         stack.append(root.left)
        #         res.append(root.val)
        #         root = root.right
        #     else:
        #         root = stack.pop()
        if root==None:
            return res
        stack.append(root)
        while stack:
            root = stack.pop()
            res.append(root.val)
            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)
        return res[::-1]


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

    print(s.postOrderTraversal(root))
