class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2 if l2 != None else None
        if l2 == None:
            return l1 if l1 != None else None
        newL = ListNode(0)
        head = newL        # 需要记录一下头节点的位置，以免之后丢失
        while l1 and l2:
            if l1.val < l2.val:
                newL.next = l1
                l1 = l1.next
            else:
                newL.next = l2
                l2 = l2.next
            newL = newL.next     # 更新newL
        if l1 == None:
            newL.next = l2
        elif l2 == None:
            newL.next = l1

        return head.next


if __name__ == '__main__':
    s = Solution()
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(4)
    n1.next = n2
    n2.next = n3

    m1 = ListNode(1)
    m2 = ListNode(3)
    m3 = ListNode(4)
    m1.next = m2
    m2.next = m3

    l1 = n1
    l2 = m1
    res = s.mergeTwoLists(l1, l2)
    if res == None:
        print('none')
    else:
        print(res.val)
        while res.next:
            res = res.next
            print(res.val)
