def twoSum(nums,start=0, target=0):
    # print('target',target)
    nums=sorted(nums)
    nums = nums[start:]
    # print('nums',nums)
    l = len(nums)
    i =0
    j = l-1
    resList = []
    if l <2:
        return []
    elif l==2:
        if nums[0]+nums[1]==target:
            return [nums]
        else:
            return []
    else:
        if nums[0]>target or nums[j]<target:
            return resList

        else:
            while i<j:
                if nums[i]+nums[j]>target:
                    j-=1
                elif nums[i]+nums[j]<target :
                    i+=1
                elif nums[i]+nums[j]==target:
                    resList.append([nums[i],nums[j]])
                    i+=1
                    j-=1
                    while i<j and nums[i]==nums[i-1]:
                        i+=1
                    while i<j and nums[j]==nums[j-1]:
                        j-=1
        # print(resList)
        return resList


def threeSum(nums,target=0):
    nums = sorted(nums)
    l = len(nums)
    resList = []
    target =0
    k=0
    if l<3:
        return []
    elif l==3:
        if nums[0]+nums[1]+nums[2]==target:
            return [nums]
        else:
            return []
    else:
        while k<l-2:
            target2 = target - nums[k]
            res = twoSum(nums, start=k + 1, target=target2)
            print('res',res)
            for r in res:

                r.extend([nums[k]])
            print('k',k)
            while nums[k]==nums[k+1] :
                k+=1
                if k+1>=l:
                    break
            k+=1
            print('res3',res)
            if len(res)>0:
                resList.append(res)
        if len(resList)==0:
            return []
        return resList[0]

def fourSum(nums,target=0):
    pass

if __name__ == '__main__':
    nums = [-2,0,1,1,2]

    print(twoSum(nums))
    # print(threeSum(nums))