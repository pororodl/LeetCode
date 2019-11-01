def uniquePaths(m, n) -> int:
    if m<=0 or n<=0:
        return 0
    arr = [[0 for i in range(n)] for j in range(m)] # 注意m 是行，n 是列
    # print(arr)
    for i in range(m):
        arr[i][0]=1
    for j in range(n):
        arr[0][j]=1
    for i in range(1,m):
        for j in range(1,n):
            arr[i][j]=arr[i-1][j]+arr[i][j-1]

    return arr[m-1][n-1]

if __name__ == '__main__':
    m = 7
    n = 3
    print(uniquePaths(m,n))