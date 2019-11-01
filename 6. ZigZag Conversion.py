def convert(s, numRows):
    res = []
    l = len(s)
    print('l',l)
    if numRows == 1:
        return s

    # 两列作为一个unit
    unit = numRows + numRows - 2
    print('unit:',unit)
    numUnits = int(l / unit)
    more = l%unit
    print('numUnits',numUnits)
    print('more',more)

    # 建一个矩阵用来填入
    # 每个unit 占的宽度为 numRows-1，有numUnit个unit 行数是numRows,
    # 列数是(numRows-1)*numUnits + 不能完整构成一个unit占用的列数，
    # 如果想要简单一点就直接建(numRows-1)*(numUnits+1)个列数

    # arr = [[0] * 2] * 3  # 这样创建有问题 三行会一样
    row = numRows
    col = (numRows-1)*(numUnits+1)
    arr = [[0 for i in range(col)] for j in range(row)]
    print(arr)

    for k in range(l):
        if k%unit<numRows:
            x = k % unit
            y = (numRows-1)*int(k/unit)

            print('x,y',x,y)
        else:
            x = numRows - (k%unit-numRows+1)-1
            y = (numRows-1)*int(k/unit)+(k%unit-numRows+1)

            print('xx,yy',x,y)
        arr[x][y]=s[k]
    print(arr)
    for i in range(row):
        for j in range(col):
            if not arr[i][j] ==0:
                res.append(arr[i][j])

    res = ''.join(res)
    return res


if __name__ == '__main__':
    s = 'PAYPALISHIRING'
    numRows = 4
    # convert(s,numRows)
    print(convert(s,numRows))
