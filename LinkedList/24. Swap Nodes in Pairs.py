# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 非递归解法
    def swapPairs(self, head: ListNode) -> ListNode:
        node = ListNode(-1)
        node.next = head
        pre = node
        while pre.next and pre.next.next:
            l1 = pre.next
            l2 = pre.next.next
            next = l2.next
            l1.next = next
            l2.next = l1
            pre.next = l2
            pre = l1
        return node.next

    # 递归解法
    def swapPairs(self, head: ListNode) -> ListNode:
        if head==None or head.next==None:
            return head
        next = head.next
        head.next = self.swapPairs(next.next)
        next.next = head
        return next