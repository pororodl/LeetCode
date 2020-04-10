def solution(nums):
    nLen = len(nums)
    i = 0
    j = nLen - 1
    while i < j:
        while i < nLen and nums[i] % 2 == 0:
            i += 1
        while j >= 0 and nums[j] % 2 == 1:
            j -= 1
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]
    s = list(map(str, nums))
    print(' '.join(s))


if __name__ == '__main__':
    # nums = list(map(int, input().split()))
    nums = [2,4,6,1,3,5]
    solution(nums)