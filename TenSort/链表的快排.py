# 仿照快排的另一种方式来对链表快排
# 不需要改变链表，只需要改变值就可以了
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def partition(self,start,end):
        num = start.val
        p = start
        q = p.next
        while q!=end:
            if q.val<num:
                p = p.next
                self.swap(p,q)
            q = q.next
        self.swap(start,p)
        return p

    def swap(self,p,q):
        temp = p.val
        p.val = q.val
        q.val =temp

    def ListQuick(self,start,end):
        if start and start!=end:
            index = self.partition(start,end)
            self.ListQuick(start, index)
            self.ListQuick(index.next, end)

if __name__ == '__main__':
    a = ListNode(4)
    b = ListNode(2)
    c = ListNode(5)
    d = ListNode(3)
    e = ListNode(7)
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

    head = a
    print('paixuqian')
    while a:
        print(a.val,end=' ')
        a = a.next

    s = Solution()
    s.ListQuick(head,h.next)

    print('paixuhou')
    while head:
        print(head.val,end=' ')
        head = head.next
