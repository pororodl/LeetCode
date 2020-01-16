class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        cand = []
        res = []
        for i in range(1,n+1):
            cand.append(i)
        A = [1,1]
        for i in range(2,10):
            t = A[i-1]*i
            A.append(t)
        while len(cand)!=0:
            count = 0
            for i in range(len(cand)):
                count+=A[len(cand)-1]

                if count>k:
                    res.append(cand[i])
                    k = k-count+A[len(cand)-1]
                    del cand[i]
                    break
                if count==k:
                    res.append(cand[i])
                    del cand[i]
                    cand.reverse()
                    res.extend(cand)
                    cand=[]
                    break

        res = list(map(str,res))
        return ''.join(res)





if __name__ == '__main__':
    s = Solution()
    n =3
    k =6
    print(s.getPermutation(n,k))