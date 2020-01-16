def onequickSort(nums,p,q):  # [p,q)索引

    i = p+1
    j = q-1
    s = nums[p]
    while i<j:
        while nums[i]<=s and i<j:
            i+=1
        while nums[j]>=s and i<j:
            j-=1
        temp = nums[i]
        nums[i]=nums[j]
        nums[j]=temp

    nums[p]= nums[i-1]
    nums[i-1] = s
    return i

# def quickSort(nums,p,q):
#     if p<q:
#         i = onequickSort(nums,0,len(nums))
#         print(nums)
#         print(i)
#         onequickSort(nums,p,i)
#         onequickSort(nums,i,q)

def quickSort(arr, left = None, right = None):
    left = 0 if not isinstance(left, (int, float)) else left
    right = len(arr) - 1 if not isinstance(right, (int, float)) else right

    if left < right:
        partitionIndex = partition(arr, left, right)
        quickSort(arr, left, partitionIndex - 1)
        quickSort(arr, partitionIndex + 1, right)
    return arr

def partition(arr, left, right):
    pivot = left     # 哨兵
    index = pivot + 1
    i = index
    while i <= right:
        if arr[i] < arr[pivot]:
            swap(arr, i, index)
            index += 1
        i += 1
    swap(arr, pivot, index - 1)
    return index - 1

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

if __name__ == '__main__':
    nums = [6,7,8,5,3,4]
    # nums = [5,4,3,2,1]

    quickSort(nums,0,len(nums)-1)

    print(nums)