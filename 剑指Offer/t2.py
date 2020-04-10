def solution(n,box):
    if n==0 or n ==1:
        return n
    box.sort(key=lambda x:x[0])
    # print(box)
    end = box[0][1]
    res1 = 1
    for i in range(1,n):
        if box[i][1]<end:
            continue
        else:
            res1+=1
            end = box[i][1]

    box.sort(key=lambda x:x[1])
    # print(box)
    end = box[0][0]
    res2 = 1
    for i in range(1, n):
        if box[i][0] < end:
            continue
        else:
            res2 += 1
            end = box[i][0]

    return max(res1,res2)

def solution2(n,box):
    wmax = 0
    lmax = 0
    for i in range(n):
        wmax = max(wmax,box[i][0])
        lmax = max(lmax,box[i][1])

    dp = [[0 for i in range(lmax+1)] for j in range(wmax+1)]
    for e in box:
        dp[e[0]][e[1]]+=1
    for i in range(1,wmax+1):
        for j in range(1,lmax+1):
            if dp[i][j]!=0:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])+dp[i][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j-1])

    return dp[wmax][lmax]


if __name__ == '__main__':
    n= int(input())
    box = []
    for i in range(n):
        w,l = map(int,input().strip().split())
        box.append([w,l])

    # print(solution(n,box))
    print(solution2(n,box))
