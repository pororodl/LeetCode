class Solution:
    # def canJump(self, nums) -> bool:
    #     '''
    #
    #     :param nums: : List[int]
    #     :return:
    #     '''
    #     return self.canJumpFromPositon(0,nums)

    def canJumpFromPositon(self, position, nums):
        if position == len(nums) - 1:
            return True
        # 最远能到的位置(索引值）是当前的位置加上当前可以走的最长的步数，和nums长度-1
        futherPosition = min(position + nums[position], len(nums) - 1)
        # 如果能从当前位置的下一个位置到最远的位置可以到终点的话，就输出True
        # for p in range(position+1,futherPosition+1,1):
        for p in range(futherPosition, position, -1):
            if (self.canJumpFromPositon(p, nums)):
                return True
        return False

    # 55题
    # def canJump(self, nums) -> bool:
    #     l = len(nums)
    #     reachPosition = l-1
    #     for p in range(l-1,-1,-1):
    #         if (p + nums[p]>=reachPosition):
    #             reachPosition = p
    #     return reachPosition==0

    # 45题  自己写有误
    def Jump(self, nums):
        l = len(nums)
        res = 0
        newPosition = 0
        while newPosition < l - 1:
            res += 1
            position = newPosition
            reach = 0
            for p in range(position + 1, position + nums[position] + 1):
                # 比较能到达的最远的位置，如果在P这个位置之后能到达最远的位置，那么newPosition 就更新为p
                reach = 0
                if nums[p] + p > reach:
                    reach = nums[p] + p
                    newPosition = p
        return res

    # 45题参考
    def jump(self, nums) -> int:
        cur_p, res = 0, 0
        if cur_p == len(nums) - 1:
            return res
        while True:
            num = nums[cur_p]
            res += 1
            max_jump = cur_p + num
            if max_jump >= len(nums) - 1:
                break
            next_jumped, next_i = -1, -1
            for i in range(cur_p + 1, min(max_jump + 1, len(nums))):    # 注意不能超过列表最大的长度
                if next_jumped < i + nums[i]:
                    next_jumped = i + nums[i]
                    next_i = i
            cur_p = next_i
        return res


if __name__ == '__main__':
    nums = [2, 3, 1, 1, 4]
    s = Solution()

    print(s.canJump(nums))
