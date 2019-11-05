def numTrees(n: int) -> int:
    if n==0 or n ==1:
        return 1
    dp = [0 for i in range(n+1)]
    print(dp)
    dp[0]=1   # 注意dp[0]是等于1的，因为当左子树或者右子树为空的时候，不能乘以0，而是要乘以1
    dp[1]=1

    for i in range(2,n+1):
        for j in range(1,i+1):
            dp[i]+=dp[j-1]*dp[i-j]
    return dp[n]

if __name__ == '__main__':
    Input = 3
    print(numTrees(Input))

