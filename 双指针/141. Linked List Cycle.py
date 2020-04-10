# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head == None:
            return False
        low = head
        fast = head
        while low!=None and fast!=None and fast.next!=None:
            if low==fast:
                return True
            low = low.next
            fast = fast.next.next

        return False