from typing import List
class NumArray:

    def __init__(self, nums: List[int]):
        self.res = []
        sum_ = 0
        for n in nums:
            sum_ +=n
            self.res.append(sum_)

    def sumRange(self, i: int, j: int) -> int:
        if i == 0:
            return self.res[j]
        ans = self.res[j]-self.res[i-1]
        return ans


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

if __name__ == '__main__':
    nums = [-2,0,3,-5,2,-1]
    obj = NumArray(nums)
    param_1 = obj.sumRange(0, 2)
    print(param_1)

