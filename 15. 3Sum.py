def twoSum(nums, start=0, target=2):
    # print('target',target)
    # nums=sorted(nums)
    nums = nums[start:]
    print('nums2', nums)
    print(target)
    l = len(nums)
    i = 0
    j = l - 1
    resList = []
    if l < 2:
        return []
    elif l == 2:
        if nums[0] + nums[1] == target:
            return [nums]
        else:
            return []
    else:

        while i < j:
            if nums[i] + nums[j] > target:
                j -= 1
            elif nums[i] + nums[j] < target:
                i += 1
            elif nums[i] + nums[j] == target:
                resList.append([nums[i], nums[j]])
                i += 1
                j -= 1
                while i < j and nums[i] == nums[i - 1]:
                    i += 1
                while i < j and nums[j] == nums[j + 1]:
                    j -= 1
    print("hello", resList)
    return resList


def threeSum(nums, start=0, target=0):
    nums = sorted(nums)

    resList = []
    nums = nums[start:]
    print(nums)
    l = len(nums)
    # target =0
    k = 0
    if l < 3:
        return []
    elif l == 3:
        if nums[0] + nums[1] + nums[2] == target:
            return [nums]
        else:
            return []
    else:
        while k < l - 2:
            target2 = target - nums[k]
            print(target2)
            print(k)
            res = twoSum(nums, start=k + 1, target=target2)
            print('res', res)
            for r in res:
                r.extend([nums[k]])
            # print('k',k)
            while nums[k] == nums[k + 1]:
                k += 1
                if k + 1 >= l:
                    break
            k += 1
            print('res3', res)
            if len(res) > 0:
                print('res4', res)
                resList.extend(res)
                print(resList)
        if len(resList) == 0:
            return []
        return resList


def fourSum(nums, target=0):
    nums = sorted(nums)
    l = len(nums)
    resList = []

    k = 0
    if l < 4:
        return []
    elif l == 4:
        if nums[0] + nums[1] + nums[2] + nums[3] == target:
            return [nums]
        else:
            return []
    else:
        while k < l - 3:
            target2 = target - nums[k]
            res = threeSum(nums, start=k + 1, target=target2)
            print('res', res)
            for r in res:
                r.extend([nums[k]])
            print('k', k)
            while nums[k] == nums[k + 1]:
                k += 1
                if k + 1 >= l:
                    break
            k += 1
            print('res3', res)
            if len(res) > 0:
                print('res4', res)
                resList.extend(res)
                print(resList)
        if len(resList) == 0:
            return []
        return resList


if __name__ == '__main__':
    nums = [-498,-492,-473,-455,-441,-412,-390,-378,-365,-359,-358,-326,-311,-305,-277,-265,-264,-256,-254,-240,-237,-234,-222,-211,-203,-201,-187,-172,-164,-134,-131,-91,-84,-55,-54,-52,-50,-27,-23,-4,0,4,20,39,45,53,53,55,60,82,88,89,89,98,101,111,134,136,209,214,220,221,224,254,281,288,289,301,304,308,318,321,342,348,354,360,383,388,410,423,442,455,457,471,488,488]

    target = -2808

    # print(twoSum(nums))
    # print(threeSum(nums, start=2, target=-5))
    print(fourSum(nums,target))
