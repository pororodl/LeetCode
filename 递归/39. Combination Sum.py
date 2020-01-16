from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        self.digui(candidates,target,0,[],res)
        return res


    def digui(self,nums,target,index,path,res):
        if target<0:
            return
        if target==0:
            res.append(path)
            return
        for i in range(index,len(nums)):
            if nums[i]>target:
                break
            self.digui(nums,target-nums[i],i,path+[nums[i]],res)

if __name__ == '__main__':
    s = Solution()
    candidates = [2,3,6,7]
    target = 7
    # candidates = [2, 3, 5]
    # target = 8
    print(s.combinationSum(candidates,target))


