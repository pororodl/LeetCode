class Solution:
    def maxProfit(self, prices) -> int:
        '''

        :param prices: : List[int]
        :return:
        '''
        res = 0
        stack = []
        for i in range(len(prices)):
            if len(stack)==0 or prices[i]<stack[-1]:
                stack.append(prices[i])
            if len(stack)!=0 and prices[i]>stack[-1]:
                res =max(prices[i]-stack[-1],res)
        return res

if __name__ == '__main__':
    prices = [7,6,4,3,1]
    s = Solution()
    print(s.maxProfit(prices))