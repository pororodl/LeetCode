# python 自带容器对象
from time import *
'''
listArray = [1,2,3]
iterName = iter(listArray)
print(next(iterName))
print(next(iterName))
print(next(iterName))
'''


# 实现__getitem__函数
class Eg1:
    def __init__(self,text):
        self.text = text
        self.subText = text.split(' ')

    def __getitem__(self, index):
        return self.subText[index]

o1 = Eg1('Hello liu lu')
for i in o1:
    print(i)

s = 'Hello liu lu'
for i in s:
    print(i,end=' ')

l = [i for i in range(100000)]
begin = time()
for i in l:
    print(i)
end = time()
print(end-begin)

# li = iter(l)
# begin = time()
# for i in li:
#     print(i)
# end = time()
# print(end-begin)