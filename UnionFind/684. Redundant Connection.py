class Solution:
    def findRedundantConnection(self, edges):
        #-> List[int]:
        ''': List[List[int]]'''
        self.eleGroupNum = []
        res = []
        self.init()
        for i in range(len(edges)):
            if self.find(edges[i][0])==self.find(edges[i][1]):
                    return edges[i]
            self.union(edges[i][0],edges[i][1])

        return res

    def init(self):
        N = 1010
        # print(N)
        for i in range(N):
            self.eleGroupNum.append(i)

    def find(self, i):
        if self.eleGroupNum[i] == i:
            return i
        return self.find(self.eleGroupNum[i])

    def union(self, i, j):
        a = self.find(i)
        b = self.find(j)
        group = min(a, b)
        self.eleGroupNum[a] = group
        self.eleGroupNum[b] = group
