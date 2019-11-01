def reverse(x):
    res = 0

    flag = False

    if x ==0 :
        return 0
    if x<-2**31 or x >2**31-1:
        return 0
    if x<0:
        flag=True
        x = -1*x
    num = []
    while x/10 != 0:
        num.append(x%10)
        x = x//10
    # print(num)
    l = len(num)
    for i in range(l):
        temp = num[i]*(10**(l-i-1))
        res+=temp
    if flag:
        res = -1*res

    if res<-2**31 or res>2**31-1:
        return 0
    return res

if __name__ == '__main__':
    x = 1534236469
    print(x)


    print(reverse(x))
