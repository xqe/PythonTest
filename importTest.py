# coding: utf-8
# python文件之间的相互调用——import

# import 模块名
# from 模块名 import 对应的类或者函数

import time
import mapTest
from classTest import Test

t0 = time.time()
time.sleep(2)
t1 = time.time()
print ("耗时%s秒"%str(t1-t0))

classTest_Test = Test(1,1)
print classTest_Test.add(3,3)
print classTest_Test.add1()