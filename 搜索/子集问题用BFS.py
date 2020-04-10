import copy
from typing import List
# def subset(li):
#     ans = [[]]
#     for i in li:
#         temp = copy.deepcopy(ans)
#         for e in temp:
#             e.append(i)
#         ans.extend(temp)
#     print(ans)
import itertools
def creat_sub(li):
    l = len(li)
    ans = [[]]
    for i in range(1,2**l):
        t = 0
        ind = []
        while i>0:
            if i%2==1:
                ind.append(t)
            t+=1
            i=i//2

        print(ind)

def letter(S):
    f = lambda x:(x.lower(),x.upper()) if x.isalpha() else x
    print(*map(f,S))
    return list(map(''.join,itertools.product(*map(f,S))))


if __name__ == '__main__':
    li = [1,5,3]
    # subset(li)
    # creat_sub(li)
    print(letter('a1n2'))
    # print(itertools.product(('a', 'A'), 1, ('n', 'N'), 2))








