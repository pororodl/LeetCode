from typing import List
class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        d = {}
        for e in B:
            temp ={}
            for i in range(len(e)):
                if e[i] not in temp:
                    temp[e[i]] =1
                else:
                    temp[e[i]]+=1
            for k,v in temp.items():
                if k not in d:
                    d[k] = v
                else:
                    d[k] = max(d[k],v)
        ans = []
        for a in A:
            flag = True
            for k,v in d.items():
                if a.count(k)<v:
                    flag = False
            if flag:
                ans.append(a)

        return ans


    # def isSubset(self,s1,s2):
    #     i = 0
    #     j = 0
    #     while

if __name__ == '__main__':
    A = ["amazon","apple","facebook","google","leetcode"]
    B = ["lo","eo"]
    s = Solution()
    s.wordSubsets(A,B)
