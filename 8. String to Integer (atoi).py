def myAtoi(str):
    str = str.lstrip()   # 将所有的空格都去掉

    # 如果去掉空格之后为空的话，就返回0
    l = len(str)
    if l==0:
        return 0

    zfFlag = False  # 用来标志正负
    opNums = 0       # 用来记录有几个操作符
    isNum = False   # 是否进入数字状态

    
    res = 0    # 最后的结果
    resList = []   # 把是数字的字符放到一个List中

    if str[0]!='+' and str[0]!='-' and (str[0]<'0' or str[0]>'9'):
        return 0

    elif str[0]=='-':
        zfFlag = True


    for i in range(l):
        if str[i]=='.':
            break
        elif isNum==False and (str[i]=='-' or str[i]=='+'):
            opNums+=1
            if opNums>1:
                break
        elif str[i]>='0' and str[i]<='9':
            isNum = True
            resList.append(str[i])

        elif str[i]==' ':
            break
        else:
            break

    print('resList',resList)
    for i in range(len(resList)):
        temp = (ord(resList[i])-ord('0'))*(10**(len(resList)-i-1))
        res+=temp
    if zfFlag:
        res = -1*res
    if res<-2**31:
        return -2**31
    if res>2**31-1:
        return 2**31-1
    return res


def atoi(s):
    s = s[::1]   # 将s反转
    num=0
    for i,v in enumerate(s):
        for j in range(0,10):
            if v ==str(j):
                num+=j*(10**i)
    return num

def atoi2(s):
    s = s[::1]
    num = 0
    for i,v in enumerate(s):
        num+=(ord(v)-ord('0'))*(10**i)
    return num

def atoi3(s):
    s = s[::1]
    num = 0
    for i,v in enumerate(s):
        t = '%s *1'%v
        n = eval(t)
        num+=n*(10**i)
    return num



if __name__ == '__main__':
    # str = '    -42'
    str = '0-1'
    # str = '+-1.2'  # ???
    print(myAtoi(str))
    # print(atoi3(s))
    # print(ord('1'))   # 49
    # print(ord('0'))   # 48
