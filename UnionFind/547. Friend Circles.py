class Solution:


    def findCircleNum(self, M) -> int:
        ''': List[List[int]]'''
        self.eleGroupNum = []
        res = 0
        self.init(M)
        for i in range(len(M)):
            for j in range(i,len(M)):
                if M[i][j]==1:
                    self.union(i,j)

        for i in range(len(M)):
            if self.eleGroupNum[i]==i:
                res +=1
        return res

    def init(self,M):
        N = len(M)
        # print(N)
        for i in range(N):
            self.eleGroupNum.append(i)


    def find(self,i):
        if self.eleGroupNum[i]==i:
            return i
        return self.find(self.eleGroupNum[i])

    def union(self,i,j):
        a = self.find(i)
        b = self.find(j)
        group = min(a,b)
        self.eleGroupNum[a] = group
        self.eleGroupNum[b] = group



if __name__ == '__main__':
    s = Solution()
    M = [[1,0,0],
         [0,1,0],
         [0,0,1]]
    print(s.findCircleNum(M))

    print(s.eleGroupNum)

