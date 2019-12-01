def digui(n):
    if n == 1:
        return 1
    ans = 0
    for i in range(1,n//2+1):
        ans+=digui(i)
    return ans+1

if __name__ == '__main__':
    N = input()
    print(N)
    N = int(N)
    print(N)
    print(digui(N))