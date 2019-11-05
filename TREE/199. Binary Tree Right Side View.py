class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode): #-> List[List[int]]
        res = []
        if root ==None:
            return res
        if root.left==root.right==None:
            return [root.val]
        queue = []
        queue.append(root)
        while queue:
            temp = []
            l = len(queue)  # 这里记录了每一层的数量
            while l>0:       # 这里为了保证输出的个数，所以加上while
                curr_node = queue.pop(0)
                temp.append(curr_node.val)
                if curr_node.left!=None:
                    queue.append(curr_node.left)
                if curr_node.right!=None:
                    queue.append(curr_node.right)
                l-=1
            res.append(temp)
        resList = []
        for e in res:
            resList.append(e[-1])


        return resList


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

    print(s.levelOrder(root))