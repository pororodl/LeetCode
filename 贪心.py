# 将一个数组平分为两堆，相加之后的差尽量小，返回差值
# 思路：将数组排序，最大的放在A，第二大的放在B，将第三大的放在B，如果此时B里面的和比A大，则
#       把第4大的放在A，如果B里面的和比A的小，就把第4大的放在B，但是要注意满足长度要求。
def MeanDivideArray(array):
    length = len(array)
    A=[]
    B=[]
    if length==0:
        return 0
    elif length==1:
        return array[0]
    else:
        array.sort(key=None,reverse=True)
        A.append(array[0])
        B.append(array[1])
        for i in range(2,length):
            if len(B)<(length+1)//2 and sum(B)<sum(A):
                B.append(array[i])
            else:
                A.append(array[i])
    print(A)
    print(B)
    print(abs(sum(A)-sum(B)))

# 如果不限制需要平分
def DivideArray(array):
    length = len(array)
    A = []
    B = []
    if length == 0:
        return 0
    elif length == 1:
        return array[0]
    else:
        array.sort(key=None, reverse=True) # 排序需要自己写
        A.append(array[0])
        B.append(array[1])
        for i in range(2, length):
            if sum(B) < sum(A):            # 求和需要自己写
                B.append(array[i])
            else:
                A.append(array[i])
    print(A)
    print(B)
    print(abs(sum(A) - sum(B)))

if __name__ == '__main__':
    a = [1,2,9,4,5,11]
    MeanDivideArray(a)
    DivideArray(a)

