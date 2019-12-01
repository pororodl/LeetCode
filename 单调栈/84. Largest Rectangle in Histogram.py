class Solution:
    def largestRectangleArea(self, heights) -> int:
        '''

        :param heights: : List[int]
        :return:
        '''
        res = 0
        l = len(heights)
        if l == 0 :
            return res
        if l ==1:
            return heights[0]
        stack = []
        stack.append(-1)
        heights.append(0)
        for i in range(l+1):
            while stack[-1]!=-1 and heights[i]<=heights[stack[-1]]:
                t = stack.pop()

                width = i-stack[-1]-1
                temp = heights[t]*width
                res = max(res,temp)

            stack.append(i)
        return res


if __name__ == '__main__':
    heights = [1,1]
    s = Solution()
    print(s.largestRectangleArea(heights))