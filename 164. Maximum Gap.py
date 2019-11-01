def maximumGap(nums):
    l = len(nums)
    res = 0
    if l < 2:
        return res
    imax = 0
    imin = 1000
    for i in range(l):
        if nums[i] > imax:
            imax = nums[i]
        if nums[i] < imin:
            imin = nums[i]
    dis = int((imax - imin) / l)

    # 把每个数字放在相应的桶里面，桶（imin，imin+dis),(imin+dis+1,imin+2dis+1),...
    # 如果桶都不为空，计算每个相邻的桶的差值res
    # 如果有一个或多个桶为空，大桶的最小值减去小桶里的最大值res


    print(imax,imin,dis)
    return res

if __name__ == '__main__':
    nums = [3,6,9,1]
    maximumGap(nums)