class Solution:
    '''
    从前word1的前i个单词变为word2的前j个单词的方法有：
    1.第一个单词的前i位变成第二个单词的前j-1位，然后再插入一个字符（d[i][j-1]+1）
    2.第一个单词的前i-1位变成第二个单词的前j位，然后再删去一个字符（d[i-1][j]+1）
    3.第一个单词的前i-1位变成第二个单词的前j-1位，然后替换最后一个字符，如果最后一个字符相同，
    即第一个单词的第i位和第二个单词的第j位相同的话，就不用替换了（d[i-1][j-1]），反之，如果不同就替换最后一位（d[i-1][j-1]+1）
因为我们需要的是第一个单词前i位到第二个单词前j位的最短编辑路径，所以就在这三种方案中取最小值就行了
    '''
    def minDistance(self, word1: str, word2: str) -> int:
        w1Len = len(word1)
        w2Len = len(word2)
        print(w2Len)
        dp = [[0 for i in range(w2Len+1)] for j in range(w1Len+1)]
        print(dp)
        for i in range(w1Len+1):
            dp[i][0] = i
        for j in range(w2Len+1):
            dp[0][j]=j
        for i in range(1,w1Len+1):
            for j in range(1,w2Len+1):
                print('i and j ',i,j)
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = 1+min(min(dp[i-1][j],dp[i][j-1]),dp[i-1][j-1]-1)
                else:
                    dp[i][j] = 1+min(min(dp[i - 1][j], dp[i][j - 1]), dp[i - 1][j - 1])
        return dp[-1][-1]





if __name__ == '__main__':
    word1 = 'horse'
    word2 = 'ros'
    s = Solution()
    print(s.minDistance(word1,word2))


