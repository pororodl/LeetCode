def longestCommonPrefix(strs) -> str:
    l = len(strs)
    if l == 0:
        return ''
    # 拿第一个作为基准，其他的和第一个作比较，如果第i位的字符元素都一样就把这个字符放到结果集中

    # 应该要比较到最短的那个字符长度
    resList = []
    i = 0
    std = strs[0]
    minLen = min(list(map(len, strs)))
    # minLen = min(list(map(lambda e: len(e),strs)))   # 两种方法都可以
    while i < minLen:
        for j in range(1, l):
            if strs[j][i] != std[i]:
                return ''.join(resList)
            else:
                continue

        resList.append(std[i])
        i += 1
    return ''.join(resList)


if __name__ == '__main__':
    strs = ["flower", "flow", "flight"]
    print(longestCommonPrefix(strs))
