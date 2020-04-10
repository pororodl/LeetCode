class Solution:
    # 只要记录前面的最小价格，将这个最小价格作为买入价格，然后将当前的价格作为售出价格，
    # 查看当前收益是不是最大收益。
    '''
    public int maxProfit(int[] prices) {
    int n = prices.length;
    if (n == 0) return 0;
    int soFarMin = prices[0];
    int max = 0;
    for (int i = 1; i < n; i++) {
        if (soFarMin > prices[i]) soFarMin = prices[i];
        else max = Math.max(max, prices[i] - soFarMin);
    }
    return max;
}
    '''

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

    def maxProfit(self, prices) -> int:
        pl = len(prices)
        minprices = float('inf')
        maxprofit = 0
        for i in range(pl):
            if prices[i]<minprices:
                minprices = prices[i]
            elif prices[i]-minprices >maxprofit:
                maxprofit = prices[i]-minprices
        return maxprofit




if __name__ == '__main__':
    prices = [7,6,4,3,1]
    s = Solution()
    print(s.maxProfit(prices))