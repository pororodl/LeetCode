# 生成器函数
class Eg3:
    def __init__(self,text):
        self.text = text
        self.sub_text=text.split(' ')

    def __iter__(self):
        for item in self.sub_text:
            yield item

class Eg4:
    def __init__(self,text):
        self.text = text
        self.sub_text = text.split(' ')

    def __iter__(self):
        yield from self.sub_text

# 生成器表达式
class Eg5:
    def __init__(self,text):
        self.text = text
        self.sub_text = text.split(' ')

    def __iter__(self):
        return (item for item  in self.sub_text)