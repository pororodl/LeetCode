class Solution:
    def isHappy(self, n: int) -> bool:
        for i in range(100):
            ele = self.n2ele(n)
            for


    def n2ele(self,n):
        ele = []
        sum = 0
        while n!= 0:
            temp = n%10
            ele.append(temp)
            sum+=temp**2
            n = n//10
        return sum

    def ele2n(self,ele):
        sum = 0
        for i,e in enumerate(ele):
            sum=sum+e*(10**i)
        return sum


if __name__ == '__main__':
    s = Solution()
    n = 129
    res = s.n2ele(n)
    print(s.n2ele(n))
    print(s.ele2n(res))
