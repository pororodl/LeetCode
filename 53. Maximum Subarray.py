def maxSubArray(nums) -> int:
    l = len(nums)
    if l == 1:
        return nums[0]
    arr = [nums[0]]
    for i in nums[1:]:
        arr.append(max(arr[-1]+i,i))   # 把当前最好的存起来？///？
        print(arr)
    return max(arr)


if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(maxSubArray(nums))