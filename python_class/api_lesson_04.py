#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021/1/12 13:11 
# @Author : Lemon_Tricy
# @QQ: 2378807189
# Copyright：湖南省零檬信息技术有限公司

"""
函数：有一段代码，重复使用到，把这段代码进行一个封装 -- 函数 --- 调用这个函数
作用： 提高代码的复用率
格式：
注意：函数名依然是一个标识符，命名规则 1-6点
def 函数名():
    函数体（真正实现具体功能的代码）
注意： 函数定义完之后，没有被调用  不会被执行的！！！
如何去调用？？--写函数名取调用
函数里面试可能会变化的内容，不建议写在函数里面-- 参数化

定义参数的类型：
1、必备参数：定义了就必须要传入的参数，不传或者少传了都会报错的
注意：必备参数必须要放在默认参数的前面
2、默认参数：如果有些参数有一些大概率的情况-- 值==默认值  ===  可以不传的-用的默认值;可以传入-- 替换默认值
3、不定长的参数：不确定是否有，也不确定有多少的这种参数--
*args：等到前面的必备参数和默认参数都接受完了之后，剩下的参数都会被这个不定长参数接受，并且以元组的个是保存
---- 多余的参数用的位置传参的方式，被*不定长参数接受
注意：位置不一定要最后
**kwargs：等到前面的必备参数和默认参数都接受完了之后，剩下的参数都会被这个不定长参数接受,并且以字典的个是保存
---- 多余的参数用的关键字传参的方式，被**不定长参数接受
注意：位置一定要最后

参数传入的方式：
1、位置传参方式：位置的顺序性==传错了位置，参数错了  ==简单，容易出错
2、关键字传参: 指定参数名进行传参的 --精确点，不容易出错
3、混合传参：位置传参必须放在关键字传参前面

断点调试：1） 方便理解原理执行过程  2）寻找问题-调试问题
1、开始调试的这行--断点
2、debug
3、点击单步执行 -- 一步一步执行

"""
# def good_job(salary,bonus,subsidy=500,*args,**kwargs):    # 定义这个函数 -- 定义参数--形参
#     print("参数salary：{}".format(salary))
#     print("参数bonus：{}".format(bonus))
#     print("参数subsidy：{}".format(subsidy))
#     print("参数args：{}".format(args))
#     print("参数kwargs：{}".format(kwargs))
#     sum1 = salary + bonus + subsidy
#     for num in args:
#         sum1 += num
#     for j in kwargs:
#         sum1 += kwargs[j]
#     print('工资总和是:{}'.format(sum1))
# 直接把调用函数的结果，赋值给了一个变量
# result = good_job(8000,2000,800,111,222,333,aa=100,bb=200,cc=300)   # 调用函数  --传参--实参
# print(result)
"""
拿到这个薪资总和，做一个判断，是不是好工作？ --10000
返回值：函数如果有一个数据需要给到调用这个函数的人去使用的话，把这个数据的变量设置为函数的返回值
1、返回值一定是在最后 ,返回值后面的代码不会被执行===标志着函数的结束
2、返回值可以没有的--None；有一个，可以有多个--- 返回值之间用逗号隔开；用元组来接受的

"""
# def good_job(salary,bonus,subsidy=500,*args,**kwargs):    # 定义这个函数 -- 定义参数--形参
#     sum1 = salary + bonus + subsidy
#     for num in args:
#         sum1 += num
#     for j in kwargs:
#         sum1 += kwargs[j]
#     return sum1 # 定义函数的返回值
#     print("6666")
# # 函数定义返回值之后，用变量接受函数的调用的时候 --- 函数的返回值
# result = good_job(8000,2000,800,111,222,333,aa=100,bb=200,cc=300)
# print('工资总和是:{}'.format(result))
# if result >= 10000:
#     print("it's a good job!")
# else:
#     print("it's not a good job!")

'''
内置函数：
print()
input()
type() 
isinstance()
len()
数据类型：str(),int(),float(),list(),tuple(),dict(),set(),bool()
字符串的内置方法：.format,index，replace，find...count
列表内置方法： append，insert，pop， remove。extend,count
字典内置方法：pop，update。get ...
range()
'''