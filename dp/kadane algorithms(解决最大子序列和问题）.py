from typing import List
def Max_subarray(nums):
    max_end_here = max_so_far = nums[0]
    for x in nums[1:]:
        max_end_here = max(x,x+max_end_here)
        max_so_far = max(max_so_far,max_end_here)
    return max_so_far


def Max_subarray_index(nums):
    start = end = 0
    max_end_here = max_so_far = nums[0]
    # for i,x in enumerate(nums[1:]):
    for i in range(1,len(nums)):
        if nums[i]>nums[i]+max_end_here:
            max_end_here = nums[i]
            start=end= i
        else:
            max_end_here = nums[i]+max_end_here
        if max_end_here>max_so_far:
            max_so_far = max_end_here
            end = i

    return max_so_far,start,end

def maxProduct1(nums: List[int]) -> int:
    if nums[0]>0:
        max_p = nums[0]    # 正数中最大的
        min_n = 0
    else:
        min_n = nums[0]    #负数中最小的
        max_p = 0
    max_so_far = max_end_here = nums[0]            # 需要比较正数
    for x in nums[1:]:
        if x>0:
            max_end_here = max(max_p*x,max_end_here)
            min_n = min_n*x
        elif x<0:
            max_end_here = max(min_n*x,max_end_here)
            max_p = max(min_n*x,max_p)
        else:
            min_n = 0
            max_p = 0
        max_end_here = max(x, max_end_here)
        max_so_far = max(max_so_far, max_end_here)
    return max_so_far


def maxProduct(nums: List[int]) -> int:
    maxProduct = nums[0]
    currPosProduct = 0
    currNegProduct = 0

    for i in nums:
        if i == 0:
            currNegProduct = 0
            currPosProduct = 0
        elif i>0:
            currPosProduct = currPosProduct*i if currPosProduct else i
            currNegProduct = currNegProduct*i if currNegProduct else 0
        elif i<0:
            newPosProduct = currNegProduct*i if currNegProduct else 0
            newNegProduct = currPosProduct*i if currPosProduct else i
            currNegProduct = newNegProduct
            currPosProduct = newPosProduct
        maxProduct = max(maxProduct,currPosProduct)
        maxProduct = max(maxProduct,currNegProduct)
    return maxProduct




if __name__ == '__main__':
    # nums = [-2,1,-3,4,0,2,1,-5, 4]
    nums = [1,-2,3]
    # nums = [2,3,-2,4]
    # nums = [-2,0,-1]
    print(Max_subarray(nums))
    # print(maxProduct(nums))
    # print(Max_subarray(nums))
    # print(-4>>1)
    # print(Max_subarray_index(nums))






    # s = None
    # a = []

    # print(True if s else False)
    # print(True if a else False)



