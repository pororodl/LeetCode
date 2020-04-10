def digui(n):
    if n == 1:
        return 1
    ans = 0
    for i in range(1, n // 2 + 1):
        ans += digui(i)
    return ans + 1


def feidigui(n):
    anslist = [0, 1]
    for i in range(2, n + 1):
        sum = 0
        for j in range(1, i // 2 + 1):
            sum += anslist[j]
        anslist.append(sum+1)
    print(anslist)
    return anslist[n]


if __name__ == '__main__':
    N = int(input())
    # print(digui(N))
    print(feidigui(N))
