def searchRange( nums, target: int):
    l = len(nums)
    i= 0
    count = 0

    while i < l:
        if nums[i]!=target:
            i += 1
            continue

        elif nums[i]==target:
            indexp = i
            break

    if i==l:
        return [-1,-1]
    else:
        for j in range(indexp+1,l):
            if nums[j]==nums[j-1]:
                count +=1
            else:
                break
    return [indexp,indexp+count]
    # return resList


if __name__ == '__main__':
    nums = [5, 7, 7, 8, 8, 10]
    target = 10
    print(searchRange(nums,target))