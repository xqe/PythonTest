# coding=utf-8
# 类

class Test:

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self, a, b):
        return a + b

    def add1(self):
        return self.a + self.b

    def sub(self, a, b):
        return a - b

class Test1(Test):
    def mul(self):
        return self.a * self.b