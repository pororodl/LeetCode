class Solution:
    def countDigitOne(self, n: int) -> int:
        if n < 0:
            return 0
        nList = []
        ntemp = n
        while ntemp!=0:
            nList.append(ntemp % 10)
            ntemp = ntemp // 10
        res = 0
        for i in range(len(nList)):
            left = n//(10**(i+1))
            print('i={}_left={}'.format(i,left))
            if nList[i]==0:
                res+= (n//(10**(i+1)))*(10**i)
                print('==0',res)
            elif nList[i] == 1:
                res+= (n//(10**(i+1)))*(10**(i))+(n%(10**(i))+1)
                print('==1',res)
            else:
                res+= (n//(10**(i+1))+1)*(10**i)
                print('>1',res)
        return res

if __name__ == '__main__':
    # n = 113
    # s = Solution()
    # print(s.countDigitOne(n))
    print(0x7fff)
    print(1808548329)



