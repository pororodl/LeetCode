import sys
import math

if __name__ == '__main__':
    n = int(input().strip())
    nums = []
    prices = []
    for line in sys.stdin:  # 当没有接受到输入结束信号就一直遍历每一行
        tempStr = line.split()
        nums.append(int(tempStr[0]))
        prices.append(int(tempStr[1]))

    perPrices = [a/b for a,b in zip(prices,nums)]
    # key = [i for i,v in sorted(enumerate(perPrices),key=lambda x:x,reverse=True)]
    # key = sorted(range(len(perPrices)),key=lambda k:perPrices[k])  # 可以实现
    dp = [float('inf')]*(n+1)
    for k in range(n):
        for j in range(1,n+1):
            g = math.ceil(j/nums[k])
            dp[j] = min(dp[j],prices[k]*g)
    print(dp[n])



