class BinaryTree:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def construct(pre,inorder,Len):
    if Len==0:
        return None
    return constructCore(pre,inorder,0,Len-1,0,Len-1)


def constructCore(pre,inorder,prestart,preend,inorderstart,inorderend):
    rootvalue = pre[prestart]
    root = BinaryTree(rootvalue)
    root.left=root.right=None

    while






if __name__ == '__main__':
    pre = map(int,input().strip().split())
    inorder = map(int,input().strip().split())
    Len = len(pre)
    construct(pre,inorder,Len)

