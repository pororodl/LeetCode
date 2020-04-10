class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 去掉倒数第N个元素，可以先找到倒数第N+1个元素
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head == None or n<=0:
            return None

        pre = self.findNthFromEnd(head,n+1)
        if pre == None:    # 如果倒数第N+1个节点是空表明第N个节点是头结点，直接删除头节点
            head = head.next
        elif pre!=None and n == 1:   # 这里要注意判断如果第N个节点是尾结点的情况，则直接删除尾节点
            pre.next = None
        else:
            pre.next = pre.next.next
        return head


    def findNthFromEnd(self, head: ListNode, n: int) -> int:
        if head == None or n <= 0:
            return None
        i = head
        j = head
        for _ in range(n - 1):
            if i.next!=None:
                i = i.next
            else:
                return None
        while i.next:
            i = i.next
            j = j.next
        return j


# 当存在什么情况的时候适合用一个头结点来避免头结点和尾结点的讨论
    # 这里是找到需要删除的节点的pre的pre
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy
        for i in range(n):
            first = first.next
        while first!=None:
            first=first.next
            second = second.next
        second.next = second.next.next
        return dummy.next





if __name__ == '__main__':
    s = Solution()
    l1 = ListNode(1)

    # l2 = ListNode(2)
    # l3 = ListNode(3)
    # l4 = ListNode(4)
    # l5 = ListNode(5)

    # l1.next = l2
    # l2.next = l3
    # l3.next = l4
    # l4.next = l5

    res = s.removeNthFromEnd(l1,1)
    if res ==None:
        print('none')
    else:
        print(res.val)
        while res.next:
            res = res.next
            print(res.val)


