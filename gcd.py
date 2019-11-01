import numpy as np
# 最大公倍数，最小公约数
# def gcd(a,b):
#     a, b = (a, b) if a >=b else (b, a)
#     if a%b == 0:
#         return b
#     else :
#         return gcd(b,a%b)
#
# def lcm(a,b):
#     return a*b//gcd(a,b)
#
# a = 25
# b = 65
# print(gcd(a,b))
# print(lcm(a,b))

# print('{:.2f}'.format(12.1))
if __name__ == '__main__':
    # ar = [1,2,3]
    # arr = np.array([1,2,3])
    arr = [[1,2],[2,3]]
    # ar1 = np.pad(ar,(1,2),'constant',constant_values=(8,9))
    arr_e = np.pad(arr,((0,2),(1,1)),'constant',constant_values=(8,9))
    # print(arr)
    # print(arr_e)
    print(arr)
    print(arr_e)
    # print(type(ar))
    print(type(arr_e))