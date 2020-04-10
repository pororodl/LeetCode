def solution(n,nums):
    i = 0
    j = n-1
    rest = 0
    while i<j:
        if i<n and nums[i]<nums[j]:
            rest+=nums[i]
            i+=1
        if j>=0 and nums[i]>nums[j]:
            rest+=nums[j]
            j-=1
        else:
            i+=1
            j-=1
    # print(rest)
    return sum(nums)+rest

if __name__ == '__main__':
    # n = int(input())
    n = 7
    # nums = list(map(int,input().split()))
    # nums = [51, 23, 52, 97,1, 97, 76, 23, 51]
    correct = [51, 23, 52,76, 97, 76,52, 23, 51]
    nums = [51, 23, 52, 97, 76, 23, 51]
    print(solution(n,nums))
    print(sum(correct))