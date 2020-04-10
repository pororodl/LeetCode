# while True:
#     try:
#         a,b = map(int,input().strip().split())
#         print(a+b),
#     except EOFError:
#         break

# A = []
# B = []
# tcase = int(input().strip())
# for i in range(tcase):
#     a,b = map(int,input().strip().split())
#     print(a,b)
#     A.append(a)
#     B.append(b)
# print(A)
# print(B)

# while True:
#     a,b = map(int,input().strip().split())
#     if a ==0 and b==0:
#         break
#     print(a+b)


def redPackage(n,d):
    left = -1
    right = n
    sumL = 0
    sumR = 0
    while left<right:
        if sumL == sumR:
            res = sumL
            left +=1
            right-=1
            sumL+=d[left]
            sumR+=d[right]
        elif sumL<sumR:
            left+=1
            sumL+=d[left]
        else:
            right -= 1
            sumR+=d[right]
    return res

if __name__ == '__main__':
    n = int(input())
    d = list(map(int,input().strip().split()))
    n = 5
    d = [1, 3, 1, 1, 4]
    print(redPackage(n,d))