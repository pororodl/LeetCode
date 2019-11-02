def climbStairs( n: int) -> int:
    dpList = [0 for i in range(n+1)]
    # print(dpList)
    if n<=2:
        return n
    else:
        dpList[0] = 0
        dpList[1] = 1
        dpList[2] = 2
        for i in range(3,n+1):
            dpList[i]=dpList[i-1]+dpList[i-2]
        print(dpList)
    return dpList[n]

if __name__ == '__main__':
    n=1
    print(climbStairs(n))