class Solution:
    def trailingZeroes(self, n: int) -> int:
        count_2 = 0
        count_5 = 0
        if n<0:
            return 0
        for i in range(2,n+1,1):
            if i%2== 0 or i%5==0:
                while i%5==0:
                    count_5+=1
                    i = i//5
                while i%2==0:
                    count_2+=1
                    i = i//2
        return min(count_2,count_5)

    def trailingZeroes2(self, n: int) -> int:
        # 只需要计算5出现的次数，怎样更快的计算5出现的次数
        count_5 = 0
        index = 1
        while n//(5**index)>0:
            count_5 += n//(5**index)
            index+=1
        return count_5


if __name__ == '__main__':
    s = Solution()
    n = 1808548329
    print(s.trailingZeroes2(n))
