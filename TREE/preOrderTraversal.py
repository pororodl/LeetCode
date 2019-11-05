class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preOrderTraversal(self,root):
        '''
        如果栈不空，输出根节点，并出栈并且输出
        将右节点压入栈（如果存在）
        将左节点压入栈(如果存在)
        :param root:
        :return:
        '''
        res = []
        if root==None:
            return res

        stack=[]
        stack.append(root)
        while stack:
            # cur = stack[-1]
            # res.append(cur.val)
            # stack.pop()
            # if cur.right:
            #     stack.append(cur.right)
            # if cur.left:
            #     stack.append(cur.left)
            root = stack.pop()
            res.append(root.val)
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
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

    print(s.preOrderTraversal(root))