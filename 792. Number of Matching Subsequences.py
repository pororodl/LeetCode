from typing import List
from collections import defaultdict
class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        A = [[] for i in range(26)]
        for i in range(len(S)):
            A[ord(S[i])-ord('a')].append(i)
        # print(A)
        ans = 0
        for word in words:
            index = -1
            toEnd = True
            for w in word:
                t = ord(w)-ord('a')
                pos = self.upper_bound(A[t],index)
                if pos == len(A[t]):
                    toEnd = False
                    break
                else:
                    index = A[t][pos]
            if toEnd:
                ans+=1
        return ans

    def upper_bound(self,nums,target):
        '''
        :param nums: 有序的数组
        :param target:
        :return: 数组nums中比target大的第一个数字的下标,如果不存在，则返回数组长度
        '''
        low,high = 0,len(nums)-1
        while low<=high:
            mid = low+(high-low)//2
            if nums[mid]<=target:
                low = mid+1
            else:
                high = mid-1
        return low



if __name__ == '__main__':
    S = 'abcdeac'
    words = ['a','ac','bb','aac']
    s = Solution()
    # print(s.numMatchingSubseq(S,words))
    waiting = defaultdict(list)
    print(waiting)
    waiting[0]= [2]
    print(waiting)

    # nums = [1,3,4,5,6]
    # print(s.upper_bound(nums,6))
