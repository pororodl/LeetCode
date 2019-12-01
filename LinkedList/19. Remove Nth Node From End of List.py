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
        if pre == None:    # 删除头节点
            head = head.next
        elif pre!=None and n == 1:   # 删除尾节点
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


