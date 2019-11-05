def getSum(a: int, b: int) -> int:
    resList = []
    mask = 0xfffffff
    ta = a & 1
    tb = b & 1
    c = ta & tb
    s = ta ^ tb
    resList.append(s)
    for i in range(31):
        a = a >> 1
        b = b >> 1
        ta = a & 1
        tb = b & 1
        s = ta ^ tb ^ c
        c = (ta & tb) | ((ta ^ tb) & c)   # & 优先级高于 ^
        resList.append(s)
    ans = 0

    for i in range(32):
        ans = ans | (resList[i] << i)
    print(resList)
    # ans = ans&mask
    if ans > 0x7fffffff:
        return ~(ans ^ 0xffffffff)
    return ans


def getMult(a, b):
    if a > b:  # 保证a是小的那个数   但是对时间复杂度不影响
        a = a ^ b
        b = a ^ b
        a = a ^ b
    aBin = []
    for i in range(32):
        ta = a & 0x1
        aBin.append(ta)
        a = a >> 1
    print(aBin)
    ans = 0
    temp = 0
    for i in range(32):
        if aBin[i] == 1:
            temp = b << i
            ans += temp
        if aBin[i] == 0:
            temp = b << i
    return ans


def getMult2(a, b):  # 可解决负数相乘的问题
    if a < 0:        # 如果是负数的话，就先转为正数，转正数使用取反加1
        aop = 1
        a = ~a + 1
    else:
        aop = 0
    if b < 0:
        bop = 1
        b = ~b + 1
    else:
        bop = 0
    ans = 0
    temp= a
    while b > 0:
        if b & 1:
            ans += temp
        b = b >> 1
        temp = temp << 1

    if aop ^ bop == 1:
        ans = ~ans+1
    return ans


if __name__ == '__main__':
    a = -12
    b = -8
    # print(getSum(a,b))
    # print(getMult(100,3))
    # print(getMult2(-100, -3))
    # print(31^2)
