# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        p = headA
        q = headB
        while p!=q:
            p = p.next if p!=None else headB
            q = q.next if q!=None else headA
        return p     # 如果有交点，返回的就是交点，如果没有交点，返回的就是最后的空




