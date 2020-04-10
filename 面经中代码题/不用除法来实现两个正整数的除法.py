def solution(x,y):
    if x<y:
        return 0
    res = 0
    while x>=y:
        mutil = 1
        while y*mutil<=(x>>1):
            mutil=mutil<<1
        res+=mutil
        x = x-y*mutil
    return res

if __name__ == '__main__':
    print(solution(27,3))

