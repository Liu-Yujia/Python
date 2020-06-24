

# 1. class learning class还有很多功能可以用

class Calculator:
      name = 'Good calculator'
      def plus(self,x,y):     # self 是默认的一个参数
            print(self.name)
            result = x + y
            print(result) 
      def minus(self,x,y):
            result = x - y
            print(result)
      def times(self,x,y):
            result = x*y
      def divide(self,x,y):
            result = x/y

cal = Calculator()
cal.name
cal.plus(10,3)

# 2. init learning 类里面比较重要的功能 “初始”

print("----------------")

class Cubic:
      # name = "A Cubic"   # 固有属性
      def __init__(self,name,high,weight,width):  # 自己输入的属性,非常常用的功能
        self.name = name
        self.h = high
        self.w = weight
        self.wi = width
c = Cubic("A defined cubic",10,13,43)
print(c.name)
print(c.h)


print('----------------')

# 3. input 功能

"""
ainput = input('give a string:')  #返回的是字符串
numinput = int(input('give a number'))  # 返回数值
print(ainput)
"""

# 4. import 模块

import time as t      # as 把一个模块做一个简化
print(t.localtime())
import numpy as np
# print(np.arrry([1,2,3]))

# 5. 输入自己的模块/脚本/py文件 输入的py文件要在同一个目录下

# import external 
#    print

# 6. continue and break 循环中常用的两个
a = True
while a:
      b = input('input a character')
      if b == 'a':
         a = False
      else:
            pass
               
print('finish run')

print('----------------')

while True:
      b = input('input a character')
      if b == 'a':
            break
      else:
            pass
      print('still in while')
print('run finish')

print('----------------')

# 7. 错误处理 try




