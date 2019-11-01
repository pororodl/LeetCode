def singleNumber(nums):
    res = []
    A = []
    B = []
    l = len(nums)
    temp = 0
    res1 = 0
    res2 = 0
    # 算出所有数异或的结果
    for i in range(l):
        temp = temp^nums[i]
    # print('temp',temp)
    # 找到结果的二进制数中为1 的一位，记录下来是哪一位j
    for j in range(32):
        if temp>>j==1:
            break
    # print('j:',j)
    # 根据第j位是1还是0将数组分为两部分，两个只出现一次的数就是分别在两个数组中
    for k in range(l):
        if nums[k]&(1<<j):
            A.append(nums[k])
        else :
            B.append(nums[k])
    # print(A)
    # print(B)
    # 对这两个数组都分别异或，分别就可以得出这两个值
    for m in range(len(A)):
        res1 = res1^A[m]
    for n in range(len(B)):
        res2 = res2^B[n]
    res.append(res1)
    res.append(res2)
    return res

if __name__ == '__main__':
    nums = [2,2,4,5,6,6]
    print(singleNumber(nums))