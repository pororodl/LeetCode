import sys
def findMedianSortedArrays(nums1, nums2) -> float:
    m, n = len(nums1), len(nums2)
    print(m,n)
    index1 = 0
    index2 = 0
    index3 = 0
    nums3 = []
    while m==0 and n!=0:
        return (nums2[(n-1)//2]+nums2[n//2])/2.0
    while m!=0 and n==0:
        return (nums1[(m-1)//2]+nums1[m//2])/2.0
    while m != 0 and n != 0:
        if nums1[index1]>=nums2[index2]:
            nums3.append(nums2[index2])
            index2+=1
            n-=1
        else:
            nums3.append(nums1[index1])
            index1+=1
            m-=1
    if m==0 and n!= 0:
        for i in range(index2,len(nums2)):
            nums3.append(nums2[i])
    if m!=0 and n==0:
        for j in range(index1,len(nums1)):
            nums3.append(nums1[j])
    print(nums3)
    if len(nums3)%2==0:
        return (nums3[(len(nums1)+len(nums2))//2]+nums3[(len(nums1)+len(nums2))//2-1])/2

    else:
        return nums3[(len(nums1)+len(nums2))//2]





if __name__ == '__main__':
    nums1 = [1,3]
    nums2 = [2]
    print(findMedianSortedArrays(nums1,nums2))