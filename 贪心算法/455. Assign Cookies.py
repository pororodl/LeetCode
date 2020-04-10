from typing import List
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g1 = sorted(g)
        s1 = sorted(s)
        gLen = len(g1)
        sLen = len(s1)
        i = j = 0
        res = 0
        print(g1)
        print(s1)
        while i<gLen and j<sLen:
            if g1[i]<=s1[j]:
                res+=1
                i+=1
                j+=1
            elif g1[i]>s1[j]:
                j+=1
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.findContentChildren([10,9,8,7],[5,6,7,8]))