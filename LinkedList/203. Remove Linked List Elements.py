# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head==None:
            return head
        if head.next==None:
            if head.val==val:
                return None
            else:
                return head
        cur1 = cur2 = ListNode(1)

        cur1.next = cur2.next= head

        while cur2.next:
            if cur2.next.val == val:
                cur2.next =cur2.next.next
            else:
                cur2 = cur2.next
        return cur1.next


if __name__ == '__main__':
    s = Solution()
    a = ListNode(6)
    b = ListNode(6)
    # c = ListNode(6)
    # d = ListNode(3)
    # e = ListNode(4)
    # f = ListNode(6)
    a.next = b
    # b.next = c
    # c.next = d
    # d.next = e
    # e.next = f
    print(s.removeElements(a,6))
    enumerate
    re