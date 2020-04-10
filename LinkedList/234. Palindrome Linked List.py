# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head==None or head.next==None:
            return True
        slow = head
        fast = head
        while fast!=None and fast.next!=None:
            slow = slow.next
            fast = fast.next.next
        if fast!=None:
            slow = slow.next
        self.cutList(head,slow)
        return self.isEqual(head,self.reverseList(slow))

    def cutList(self,head,cutNode):
        while head.next!=cutNode:
            head = head.next
        head.next = None

    def reverseList(self,head):
        newHead = ListNode(-1)
        while head!=None:
            next = head.next
            head.next = newHead.next
            newHead.next = head
            head = next
        return newHead.next

    def isEqual(self,l1,l2):
        while l1!=None and l2!=None:
            if l1.val!=l2.val:
                return False
            l1 = l1.next
            l2 = l2.next
        return True


