# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        p = head
        while p!=None:
            q = p
            while q and q.val==p.val:
                q = q.next
            p.next = q
            p = p.next

        return head