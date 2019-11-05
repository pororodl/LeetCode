def longestValidParentheses(s: str) -> int:
    l = len(s)
    stackList = []
    res = 0
    start = 0
    for i in range(l):
        if s[i] == '(':
            stackList.append(i)
        # 当碰到')'
        elif s[i] == ')':
            if len(stackList) == 0:
                start = i + 1
            else:
                stackList.pop(-1)
                if len(stackList) == 0:
                    res = max(res, i - start + 1)
                else:
                    res = max(res, i - stackList[-1])
    return res


if __name__ == '__main__':
    s = "()((())"
    print(longestValidParentheses(s))
