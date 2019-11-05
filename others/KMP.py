def KMP(s,p):
    '''

    :param s:
    :param p:
    :return: int 返回模式串在s串中的位置
    '''

    next = getNext(p)
    i = 0
    j = 0
    slen = len(s)
    plen = len(p)

    while i<slen and j<plen:
        if j==-1 or s[i]==p[j]:
            i+=1
            j+=1
        else:
            j = next[j]
    if j == plen:
        return i-j
    else:
        return -1


def getNext(p):
    '''
    计算next数组
    :param p: 字符串
    :return: next 数组
    '''
    l = len(p)
    next = [0 for i in range(l)]

    next[0]=0
    for i in range(1,l):
        if p[i]==p[next[i-1]]:
            next[i]=next[i-1]+1
        else:
            k = next[i-1]
            while k>0 and p[i]!=p[k]:
                k = next[k-1]
            if p[i]==p[k]:
                next[i]=next[k]+1
    # 将整个list后移一位，第一位赋值-1
    for i in range(l-1,0,-1):
        next[i]=next[i-1]
    next[0]=-1
    return next

if __name__ == '__main__':
    s = 'bsadjiababaakkl'
    p = 'ababaa'


    # print(getNext(p))
    print(KMP(s,p))


