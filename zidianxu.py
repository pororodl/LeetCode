class Solution:
    zhs = [[0 for i in range(50)] for j in range(50)]

def init():

    Solution.zhs[0][0] = 0
    Solution.zhs[1][0] = 1
    Solution.zhs[1][1] = 1
    for i in range(2, 30):
        Solution.zhs[i][0] = 1
        Solution.zhs[i][i] = 1
        for j in range(1, i):
            Solution.zhs[i][j] = Solution.zhs[i - 1][j - 1] + Solution.zhs[i - 1][j]

def calzhs(m,n):
    # 计算组合数m 下标，n 上标，返回
    # 存组合数的结果，利用杨辉三角
    return Solution.zhs[m][n]


def zidianxu(string1:str):
    nlen = len(string1)
    if nlen>6:
        return 0
    if nlen == 1:
        return ord(string1[0])-ord('a')+1
    # 判断是否是连续的升序
    flag = True
    for i in range(nlen-1):
        if ord(string1[i])>=ord(string1[i+1]):
            return 0
        if ord(string1[i+1]) - ord(string1[i])!=1:
            flag = False
    standard = 'abcdefghijklmnopqrstuvwxyz'
    # 递归的出口


    if flag and string1[0]=='a':
        ans = 0
        for i in range(nlen):
            ans += calzhs(26,i)
        return ans
    if flag:
        ans = 0
        std = standard[0:nlen]
        n = ord(string1[0])-ord('a')
        for i in range(1,n+1):
            ans += calzhs(26-i,nlen-1)
        return zidianxu(std)+ans

    startIndex = ord(string1[0])-ord('a')
    std = standard[startIndex:startIndex+nlen]
    return zidianxu(std)+zidianxu(string1[1:])-zidianxu(std[1:])

def i_th(k):
    standard = 'abcdefghijklmnopqrstuvwxyz'
    slen = 0
    for i in range(26):
        s = standard[0:i+1]
        if zidianxu(s)==k:
            return s
        elif zidianxu(s)>k:
            slen = i
            break
    if slen == 0:
        slen = 6
    std = standard[0:slen]
    ans = ''
    print(slen)
    for i in range(slen):
        start = 0
        anslen = len(ans)
        if anslen>0:
            start = 0 + ord(ans[-1]) - ord('a') + 1
        while start+slen-anslen<=26:
            ts = ans+standard[start:start+slen-anslen]
            if zidianxu(ts)==k:
                return ts
            if zidianxu(ts)>k:
                ans +=standard[start-1]
                break
            start+=1
    return ans






if __name__ == '__main__':
    # print(calzhs(5,3))

    init()
    n = int(input())
    while n>0:
        s = input()
        print(zidianxu(s))
        print(i_th(zidianxu(s)))
        n-=1
