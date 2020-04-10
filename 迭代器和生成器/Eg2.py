# 如果要自定义一个可以迭代的对象的话，必须实现iter函数，在iter函数中返回一个迭代器
# 这个迭代器需要自己定义，迭代器需要实现__iter__函数和__next__函数，在__iter__函数中，只需要返回自身就可以了
# 即return self
# 在__next__中，需要自己实现一个迭代的过程
class Eg2:
    def __init__(self,text):
        self.text = text
        self.subText = text.split(' ')

    def __iter__(self):
        return Eg2Iterator(self.subText)

class Eg2Iterator:#迭代器对象
    def __init__(self,subText):
        self.subText = subText
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            sub_text = self.subText[self.index]
        except IndexError:
            raise StopIteration()
        self.index+=1
        return sub_text


o2 = Eg2('hello liu lu')
it = Eg2Iterator('hello')
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

# for i in o2:
#     print(i)