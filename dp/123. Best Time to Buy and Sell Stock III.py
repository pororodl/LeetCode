from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pl = len(prices)
        flag = False
        for i in range(pl-1):
            if prices[i]<prices[i+1]:
                flag = True
        if flag==False:
            return 0


        maxans = 0
        for i in range(0,pl):
            ansL = self.maxProfit1(prices,0,i)
            ansR = self.maxProfit1(prices,i+1,pl-1)


            maxans = max(maxans,ansL+ansR)
            # print(maxans)
        print(maxans)
        return maxans


    def maxProfit1(self, prices,start,end) -> int:
        # pl = len(prices)
        if start>= end:
            return 0

        minprices = float('inf')
        maxprofit = 0
        for i in range(start,end+1):
            if prices[i]<minprices:
                minprices = prices[i]
            elif prices[i]-minprices >maxprofit:
                maxprofit = prices[i]-minprices
        return maxprofit

if __name__ == '__main__':
    prices = [1, 2, 3,4,5]
    s = Solution()
    print(s.maxProfit(prices))