def singleNumber(nums) -> int:
    arr = [0] * 32  # 为什么是32
    res = 0
    for i in range(len(nums)):
        for j in range(32):
            arr[j] += nums[i] >> j & 0x1


    if arr[-1]%3==0:
        for k in range(32):
            if arr[k] % 3 == 1:
                res += 1 << k  # 需要解决res为负数的问题
    else:
        for k in range(32):
            if arr[k] % 3 == 0:
                res += 1 << k
        res=~res

    return res

if __name__ == '__main__':
    Input = [-2,-2,1,1,-3,1,-3,-3,-4,-2]
    print(singleNumber(Input))