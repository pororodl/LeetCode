def uniquePathsWithObstacles(obstacleGrid) -> int:
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    print('m,n',m,n)
    arr = [[0 for i in range(n)] for j in range(m)]

    if m ==1 and n==1:
        if obstacleGrid[0][0]==0:
            return 1
        if obstacleGrid[0][0]==1:
            return 0


    elif m!=1 and n!=1:
        for i in range(m):
            if obstacleGrid[i][0]!=1:
                arr[i][0]=1
            else:
                break
        print('hang')
        print(arr)

        for j in range(n):
            if obstacleGrid[0][j]!=1:
                arr[0][j] = 1
            else:
                break
        print('lie')
        print(arr)

        for k in range(1,m):
            for l in range(1,n):
                if obstacleGrid[k][l]==1:
                    arr[k][l]=0
                else:
                    arr[k][l]=arr[k-1][l]+arr[k][l-1]
        print(arr)
        return arr[m-1][n-1]

    elif m==1 and n!=1:
        for j in range(n):
            if obstacleGrid[0][j]!=1:
                arr[0][j] = 1
            else:
                break


        print('lie')
        print(arr)
        return arr[m-1][n-1]
    else:
        for i in range(m):
            if obstacleGrid[i][0]!=1:
                arr[i][0]=1
            else:
                break
        print('hang')
        print(arr)
        return arr[m - 1][n - 1]

if __name__ == '__main__':
    # Input = [
    #     [0,0,0],
    #     [0,1,0],
    #     [0,0,0]
    # ]
    Input=[[0,0],[1,0]]
    res = uniquePathsWithObstacles(Input)
    print(res)

