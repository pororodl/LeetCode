class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        b = int(c**0.5)

        while a<=b:
            sum = a**2+b**2
            if sum==c:
                return True
            elif sum<c:
                a+=1
            else:
                b-=1
        return False

if __name__ == '__main__':
    s = Solution()
    print(s.judgeSquareSum(4))

