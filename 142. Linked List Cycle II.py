class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head==None or head.next==None:
            return None
        if head.next==head:
            return head
        low = head
        fast = head
        hascycle = False
        while fast.next!=None and fast.next.next!=None:
            low = low.next
            fast = fast.next.next
            if low==fast:
                hascycle = True
                break
        if hascycle:
            meet = low

            i = head
            while i!=meet:
                i = i.next
                meet=meet.next
            return i

        return None