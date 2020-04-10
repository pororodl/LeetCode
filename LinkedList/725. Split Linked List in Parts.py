from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        Len = 0
        cur = root
        while cur!=None:
            cur = cur.next
            Len+=1
        mod = Len%k
        size = Len//k
        res = [None]*k
        cur = root
        k_i =0
        while cur!=None and k_i<k:
            res[k_i] = cur
            curSize = size+1 if mod>0 else size
            mod-=1
            for size_i in range(0,curSize-1):
                cur=cur.next
            next = cur.next
            cur.next = None
            cur = next
            k_i+=1

        return res


