# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum: int) :
        '''

        :param root: : TreeNode
        :param sum:
        :return: -> List[List[int]]
        '''
        res = [[]]
        if root == None:
            return []
        if root.left ==None and root.right == None:
            if root.val == sum:
                res[0].append(root.val)
                return res
            return []
        ans1 = self.pathSum(root.left,sum-root.val)
        ans2 = self.pathSum(root.right,sum-root.val)
        res = []
        if len(ans1)!= 0:
            for e in ans1:
                e.insert(0,root.val)
                res.append(e)
        if len(ans2)!= 0:
            for e in ans2:
                e.insert(0,root.val)
                res.append(e)
        return res


if __name__ == '__main__':
    a = [1]
    print(a == None)