class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
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
        return j.val



if __name__ == '__main__':
    s = Solution()
    l1 = ListNode(1)
    l1.next =None
    # l2 = ListNode(2)
    # l3 = ListNode(3)
    # l4 = ListNode(4)
    # l5 = ListNode(5)
    #
    # l1.next = l2
    # l2.next = l3
    # l3.next = l4
    # l4.next = l5

    print(s.findNthFromEnd(l1,1))
