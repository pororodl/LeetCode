from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1stack = self.buildStack(l1)
        l2stack = self.buildStack(l2)
        carry = 0
        newL = ListNode(-1)
        while l1stack or l2stack or carry!=0:
            x = 0 if len(l1stack)==0 else l1stack.pop()
            y = 0 if len(l2stack)==0 else l2stack.pop()
            sum = x+y+carry
            val = sum%10
            curL = ListNode(val)
            curL.next=newL.next
            newL.next = curL
            carry = sum//10
        return newL.next


    def buildStack(self,l:ListNode)-> List : # 用list模拟栈
        stack = []
        while l:
            stack.append(l.val)
            l = l.next
        return stack
