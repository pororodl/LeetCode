from typing import List
import math
class NumArray0: # 超时

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.res = [0]
        sum_ = 0
        for n in nums:
            sum_ +=n
            self.res.append(sum_)
        print(self.res)
    def update(self, i: int, val: int) -> None:
        #
        for m in range(i+1,len(self.res)):
            self.res[m]+=(val-self.nums[i])
        self.nums[i] = val
        # print('update:',self.res)

    def sumRange(self, i: int, j: int) -> int:
        return self.res[j+1]-self.res[i]

class NumArray1: # 超时

    def __init__(self, nums: List[int]):
        self.nums = nums

    def update(self, i: int, val: int) -> None:
        self.nums[i] = val
        # print('update:',self.res)

    def sumRange(self, i: int, j: int) -> int:
        ans = 0
        for m in range(i,j+1):
            ans+=self.nums[m]
        return ans

class NumArray2: # Accepted

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.l = int(math.sqrt(len(self.nums)))   # 每个块的长度
        if self.l == 0:   # 要注意判断 nums为空的情况
            self.b = [0]
        else:
            self.len = math.ceil(len(self.nums) / self.l)  # 向上取整,一共有多少个块
            self.b = [0 for i in range(self.len)]
            for i in range(len(self.nums)):
                self.b[i // self.l] += self.nums[i]


    def update(self, i: int, val: int) -> None:
        self.b[i//self.l] +=val-self.nums[i]
        self.nums[i] = val
        # print('update:',self.res)

    def sumRange(self, i: int, j: int) -> int:
        ans = 0
        startBlock = i//self.l
        endBlock = j//self.l
        if startBlock == endBlock:
            for k in range(i,j+1):
                ans +=self.nums[k]
        else:
            for k in range(startBlock+1,endBlock):
                ans += self.b[k]
            for m in range(i,(startBlock+1)*self.l):
                ans += self.nums[m]
            for n in range(endBlock*self.l,j+1):
                ans+=self.nums[n]
        return ans

class NumArray3: # 线段树 Accepted
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.n_len = len(self.nums)
        if self.n_len ==0:
            self.tree = [0]
        else:
            self.tree = [0 for i in range(2*self.n_len)]
            i =  self.n_len
            j = 0

            while i<2*self.n_len:
                self.tree[i] = self.nums[j]
                i +=1
                j +=1

            for i in range(self.n_len-1,-1,-1):
                self.tree[i] = self.tree[2*i]+self.tree[2*i+1]
            print(self.tree)

    def update(self, i: int, val: int) -> None:
        i = self.n_len+i
        self.tree[i] = val

        while i//2!=0:
            i = i//2
            self.tree[i]=self.tree[2*i]+self.tree[2*i+1]
        print(self.tree)

    def sumRange(self, i: int, j: int) -> int:
        ans = 0
        ipos = i+self.n_len
        jpos = j+self.n_len
        while ipos<=jpos:
            if ipos%2 ==1:
                ans+= self.tree[ipos]
                ipos+=1
            if jpos%2 ==0:
                ans+=self.tree[jpos]
                jpos-=1
            ipos =ipos//2
            jpos =jpos//2

        return ans





# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)

if __name__ == '__main__':
    nums = [7,2,7,2,0,3,4,6,9]
    obj = NumArray3(nums)
    obj.update(4,6)
    obj.update(0, 2)
    obj.update(0, 9)
    param_2 = obj.sumRange(4,4)
    print(param_2)
    obj.update(3, 8)
    param_3 = obj.sumRange(0, 4)
    print(param_3)
    obj.update(4, 1)
    param_4 = obj.sumRange(0, 3)
    print(param_4)
    param_5 = obj.sumRange(0, 4)
    print(param_5)




