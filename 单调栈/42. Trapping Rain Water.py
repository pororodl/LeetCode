class Solution:
    def trap(self, height) -> int:
        '''

        :param height: : List[int]
        :return:
        '''
        res = 0
        l = len(height)
        if l<3:
            return res
        L = [0]*l
        R = [0]*l
        for i in range(1,l-1):
            L[i] = max(L[i-1],height[i-1])
            R[l-1-i] = max(R[l-i],height[l-i])


        for i in range(l):
            if L[i]>height[i] and R[i]>height[i]:
                res += min(L[i],R[i])-height[i]

        return res

    def trap2(self, height) -> int:
        res = 0
        l = len(height)
        if l < 3:
            return res
        stack = []  # 栈中保存的是每个元素的下标
        for i in range(l):
            # 出栈的条件是，栈不为空和当前的元素大于栈顶元素，维护一个递减的栈，有出栈操作时注意一定要判断栈是否为空
            while len(stack)!= 0 and height[i]>height[stack[-1]]:
                t = stack.pop()
                if len(stack)==0:
                    break
                if height[t]==height[stack[-1]]:
                    continue
                width = i-stack[-1]-1
                h = min(height[stack[-1]],height[i])   # 取右边比height[t]大的元素和左边比height[t]小的元素
                res += width*(h-height[t])             # 然后减去取的栈顶的元素的高度
            # 进栈
            stack.append(i)
        return res

if __name__ == '__main__':
    height = [3,0,1,0,3]
    s = Solution()
    print(s.trap2(height))
