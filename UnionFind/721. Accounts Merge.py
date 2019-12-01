class Solution:
    def accountsMerge(self, accounts):
        '''

        :param accounts: : List[List[str]]
        :return: -> List[List[str]]
        '''
        mail2index = {}
        for ele in accounts:
            for i in range(1,len(ele)):
                if not ele[i] in mail2index:
                    mail2index[ele[i]]=len(mail2index)

        self.eleGroupNum = [-1]*len(mail2index)
        res = []

        # 将所有第一个出现的邮箱的组别分配好
        for i, ele in enumerate(accounts):
            self.eleGroupNum[mail2index[ele[1]]] = i
            res.append([ele[0]])

            if len(ele)>2:
                for j in range(1,len(ele)):
                    self.eleGroupNum[mail2index[ele[j]]] = mail2index[ele[1]]
                    res[i].extend(ele[j])
            res[i].extend(ele[1])
        return res








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



if __name__ == '__main__':
    s = Solution()
    accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"],
                ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
    print(s.accountsMerge(accounts))
    # print(s.eleGroupNum)


