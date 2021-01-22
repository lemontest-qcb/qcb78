#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021/1/9 18:52 
# @Author : Lemon_Tricy
# @QQ: 2378807189
# Copyright：湖南省零檬信息技术有限公司
'''
1. 下面哪些不能作为标识符？-- 标识符命名
1、find 2、 _num 3、7val 4、add. 5、def 6、pan 7、-print 8、open_file 9、FileName
10、print 11、INPUT 12、ls 13、user^name 14、list1 15、str_
答案：
1、find --- ok
2、_num -- ok
3、7val -- 不可以，不能以数字开头
4、add.  -- 不可以，包含.
5、def -- 不可以，关键字不能用
6、pan -- 可以
7、-print -- 不可以，- 不支持
8、open_file -- ok
9、FileName -- ok== 大驼峰的方式 LemonTricy  Pythonclass --小驼峰 --了解
10、print  == ok，但是不推荐使用 ，影响函数的使用  list  dict --内置函数名字
11、INPUT == ok，INPUT ！=input
12、ls == ok
13、user^name  == 不可以
14、list1  == ok，推荐的
15、str_  == ok
'''

"""
字符串操作：
1、取值：每个元素都有的位置 -- 索引 ==从0开始   str1[4]
取最后一个元素：-1  == 负数的取法 
2、取多个值： 切片 == 指定[索引头:索引尾:步长] == 规则：取头不取尾
头默认值：从0开始
索引尾默认值：最后
步长默认值：为1
3、获取长度：len() ---计算变量的长度，并返回这个数字
4、常用方法：
"""
# 定义了一个字符串
str1 = 'hello lemomban!'
#       01234567891011121314
# print(str1[4])
# print(str1[-1])
# print(str1[:len(str1):])
# print(len(str1))
# 获取某个元素的索引 --
# print(str1.index('y'))   # 没有找到元素会报错 -- 代码会停止运行
# print(str1.find('y'))  # 没有找到元素不会报错，返回-1-- 代码不会停止运行
# # 统计个数：
# print(str1.count('l'))
# # 元素替换-- 旧的内容，新的内容
# print(str1.replace('lemomban','Python'))

'''
Python运算符：1 + 2 = 3   运算数，+ = 运算符
1、算术运算符：+ - * / 
'''
# +  1、 两个数字的相加 ==数学  2、字符串的拼接
# num = 100
# print(10 + 20)
# print('tricy' + 'lemon')
# print(str(num) + 'lemon')
# # 数据类型的强制转换：str() int() float()
# # input() -- 获取从控制台进行输入内容== 输入的任何内容都是字符串
# num1 =  int(input("请输入一个数字："))
# print(type(num1))
# print(num1+1)
# - 两个数字相减  ==不支持字符串
# print(20 - 10)
# # *  1、表示两个数字相乘的结果  2、字符串的重复输出
# print(2 * 3)
# print('I love you' * 3000)
# # /  --结果是float
# print(10/2)
# 2、赋值运算符--符号右边的内容赋值给左边内容  = ，+=，-=
# a = 10
# a += 5 #a = a + 5
# a -= 10
# print(a)
# 3、比较运算符 > < == <=  >= |  !=  ==  可以判断字符串是否相等-- 用于断言 --  运算结果是布尔值 === 运算结果是一个bool值
# print(4 >= 6)
# print("登录成功"=="登录成功")
# 4、逻辑运算符： and-与  or -或 not -非  ===  and --真真为真  or - 假假为假  ==== 运算结果是一个bool值
print(not 5<9)
# 5、成员运算符：in   not in   == 运算结果是一个bool值
str2 = "hello Python"
print("P" in str2)


