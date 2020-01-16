from typing import List

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        gLen = len(groupSizes)

        d = {}
        for i in range(gLen):
            if groupSizes[i] not in d:
                d[groupSizes[i]]=[i]
            # elif groupSizes[i] in d and isFull[i]==True:

            else:
                d[groupSizes[i]].append(i)
        ans = []
        count = 0
        for k,v in d.items():
            temp = []
            for i in v:
                temp.append(i)
                count+=1
                if count==k:
                    ans.append(temp)
                    count=0
                    temp = []

        return ans

if __name__ == '__main__':
    # groupSizes = [2, 1, 3, 3, 3, 2]
    groupSizes = [3,3,3,3,3,1,3]
    s = Solution()
    print(s.groupThePeople(groupSizes))