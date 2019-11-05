def minPathSum(grid) -> int:
    m = len(grid)  # 行数
    n = len(grid[0])  # 列数
    if m ==0 or n==0:
        return 0
    dp = [[0 for i in range(n)] for j in range(m)]
    print(dp)
    # 更新第一行
    dp[0][0]=grid[0][0]
    for i in range(1,n):
        dp[0][i]=dp[0][i-1]+grid[0][i]
    # 更新第一列
    for j in range(1,m):
        dp[j][0]=dp[j-1][0]+grid[j][0]
    # 更新其他位置
    for k in range(1,m):
        for l in range(1,n):
            dp[k][l]=min(dp[k][l-1],dp[k-1][l])+grid[k][l]

    return dp[m-1][n-1]

if __name__ == '__main__':
    Input=[
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    print(minPathSum(Input))
