# 采用的是中心展开法
# 只解决了有对称中心的回文子串
def longestPalindrome(s):
    length = len(s)
    print('s lengeth:',length)
    if length == 0:
        return ''
    if length == 1:
        return s
    output = []
    maxLen = 0
    for i in range(1, length-1):
        curLen = 1
        k = min(i, length - i -1)
        for j in range(1, k+1):
            if s[i - j] == s[i + j]:
                curLen += 2
                if curLen >maxLen:
                    output = s[i - j:i + j + 1]
                    maxLen = curLen
                else:
                    maxLen = maxLen
            else:
                break
    return output

# 采用在串中间加'#'的方法，来解决没有对称中心的问题
def solution2(s):
    length = len(s)
    # print('s lengeth:', length)
    if length == 0:
        return ''
    if length == 1:
        return s
    expand = []
    for e in s:
        expand.append('#')
        expand.append(e)
    expand.append('#')
    print('expand', expand)
    expLength = len(expand)
    output = []
    maxLen = 0
    for i in range(1, expLength-1):
        curLen = 1
        k = min(i, expLength - i-1)
        for j in range(1, k + 1):
            if expand[i - j] == expand[i + j]:
                curLen += 2
                if curLen > maxLen:
                    output = expand[i - j:i + j + 1]
                    maxLen = curLen
                else:
                    maxLen = maxLen
            else:
                break
    for o in output:
        if o=='#':
            output.remove('#')
    output = ''.join(output)
    return output

# 还可以采用dp来解决
def dp(s):
    l = len(s)
    arr = [[False for m in range(l)] for n in range(l)]


    print(arr)

if __name__ == '__main__':
    s = 'babad'
    # print(longestPalindrome(s))
    # print(solution2(s))
    dp(s)