class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head==None:
            return False
        if head.next==None:
            return False
        if head.next==head:
            return True
        low = head
        fast = head
        while fast.next!= None:
            low = low.next
            fast = fast.next.next
            if low==fast:
                return True
            if fast==None:
                return False
        return False



