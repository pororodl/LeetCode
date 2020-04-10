from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        Len = len(numbers)
        index1 = 0
        index2 = Len-1
        while index1<index2:
            if numbers[index1]+numbers[index2]==target:
                return [index1+1,index2+1]
            elif numbers[index1]+numbers[index2]<target:
                index1+=1
            else:
                index2-=1


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([2,7,11,15],9))