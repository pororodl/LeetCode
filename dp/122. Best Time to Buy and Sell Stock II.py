class Solution:
    def maxProfit(self, prices) -> int:

        '''
        :param prices: : List[int]
        :return:
        '''
        pl = len(prices)
        res = 0
        i = 0
        while i<pl-1 :
            while i<pl-1 and prices[i]>=prices[i+1]:
                i+=1
            b = prices[i]
            while i<pl-1 and prices[i]<=prices[i+1]:
                i+=1
            s = prices[i]
            res += s-b

        return res


