from typing import List
class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        longestWord = ''
        for target in d:
            l1 = len(longestWord)
            l2 = len(target)
            print(target)
            if l1>l2 or (l1==l2 and self.compareTo(longestWord,target)>0):
                continue
            elif self.isSubString(s,target):
                # print('s',s,'target',target)
                # print('isSub:',self.isSubString(s,target))
                longestWord = target

        return longestWord

    def compareTo(self,s1,s2) -> bool:    # 比较字典序
        l1 = len(s1)
        p = 0
        while p<l1:
            if ord(s1[p])==ord(s2[p]):
                p+=1
                continue
            if ord(s1[p])<ord(s2[p]):
                return 1
            else:
                return -1
        if p==l1:
            return 0

    def isSubString(self,s,t):
        l1 = len(s)
        l2 = len(t)
        if l1<l2:
            return False
        i = j = 0
        while j<l2 and i<l1:
            if s[i]==t[j]:
                i+=1
                j+=1
            else:
                i+=1
        if j == l2 and i<=l1:
            return True
        return False

if __name__ == '__main__':
    s = Solution()
    # print(s.compareTo('aaa','aaa'))
    print(s.isSubString('aaa','aaa'))
    print(s.findLongestWord("aaa",["aaa","aa","a"]))