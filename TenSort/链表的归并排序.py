# 仿照快排的另一种方式来对链表快排
# 不需要改变链表，只需要改变值就可以了
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def merge(self,p,q):
        new =l = ListNode(0)
        while p and q:
            if p.val<=q.val:
                new.next = p
                p=p.next
            else:
                new.next=q
                q = q.next
            new = new.next
        new.next = p or q
        return l.next

    def mergeSort(self,head):
        if head == None or head.next==None:
            return head
        slow = head
        fast = head.next    # 这里fast从head.next开始，是我们要获得中间元素的前一个元素来获取中间元素作为第二段的头和方便断开
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next    # 得到后半段的头
        slow.next = None   # 把前半段和后半段断开
        return self.merge(self.mergeSort(head),self.mergeSort(mid))

if __name__ == '__main__':
    a = ListNode(4)
    b = ListNode(2)
    c = ListNode(5)
    d = ListNode(3)
    e = ListNode(5)
    f = ListNode(9)
    g = ListNode(0)
    h = ListNode(1)

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    f.next = g
    g.next = h
    h.next = None
    s = Solution()
    res = s.mergeSort(a)
    while res:
        print(res.val,end=' ')
        res = res.next


