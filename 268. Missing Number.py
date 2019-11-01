def missingNumber(nums):
    l = len(nums)
    print(l)
    res = 0
    for i in range(l):
        res = res ^ i
        print('{0}次异或结果{1}'.format(i,res))
        res = res ^ nums[i]
        print('{0}次异或结果{1}'.format(i, res))
    res = res ^ l
    return res

if __name__ == '__main__':
    nums = [0,1,3,4,5]
    print(missingNumber(nums))

    p