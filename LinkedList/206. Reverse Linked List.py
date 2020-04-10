# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 递归（注意整体思想）
    def reverseList(self, head: ListNode) -> ListNode:
        if head==None or head.next==None:
            return head
        next = head.next            # 记录下要反转前的头，将会是反转后的尾
        newHead = self.reverseList(next)  #反转部分
        next.next = head              # 将头接到反转后的链表后
        head.next = None              # 原先的头就是尾，就要把空接在后面
        return newHead

    # 头插法
    def reverseList(self,head):
        newHead = ListNode(-1)
        while head!=None:
            cur = head.next
            head.next = newHead.next
            newHead.next = head   # 把假的头节点连接到
            head = cur
        return newHead.next


