from typing import List
import copy
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        ans=[[]]
        for i in range(len(S)):
            if ord('A')<= ord(S[i])<= ord('z'):
                temp = copy.deepcopy(ans)
                for e in ans:
                    e.append(S[i].lower())
                for t in temp:
                    t.append(S[i].upper())
                ans.extend(temp)
            else:
                for a in ans:
                    a.append(S[i])
        # res = []
        for i in range(len(ans)):
            ans[i] = ''.join(ans[i])
        return ans

if __name__ == '__main__':
    s = Solution()
    S = 'aab2'
    print(s.letterCasePermutation(S))