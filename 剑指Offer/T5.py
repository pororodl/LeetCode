def replaceSpace(s):
    sLen = len(s)
    # 1.遍历s计算出空格的数量
    spaceNum = 0
    for i in range(sLen):
        if s[i]==' ':
            spaceNum +=1
    newLen = sLen+2*spaceNum
    res = []*newLen


