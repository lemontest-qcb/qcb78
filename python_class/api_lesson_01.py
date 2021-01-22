#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021/1/8 20:42 
# @Author : Lemon_Tricy
# @QQ: 2378807189
# Copyright：湖南省零檬信息技术有限公司

"""
标识符：Python里凡是自己取名字：project   Python package    Python file  变量 函数
命名规则：  --记住
1、只能包含数字、字母、下划线 == 英文
2、不能以数字开头
3、不能使用关键字 ：什么是关键字？ == python 已经定义好的，有自己特殊意义的字符  == 不需要记，报错
import keyword
print(keyword.kwlist)
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue',
 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in',
'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

4、建议：不同数字和字母之间用下划线隔开  python_77_78  --  方便阅读
5、取名字  见名知义
PeP8规范  ， Python之禅  == 编码规范  ==扩展了解

运行：
1、右键 run

注释方法：
1、单行注释： # 后面的内容
2、多行注释：""" """   ''' ''' 
3、快捷键 注释 ctrl + /   == 注释 取消注释
注释作用：
1、方便阅读代码-- 自己+别人  解释干什么用的
2、 需求变更了，一段代码没有用  -- 不会影响代码运行，以后加回来 

语法规则：
1、 Python代码对缩进敏感 ，代码需要顶格编写 
除非 父子（层级）关系  ==  if  函数 循环
2、Python区分大小写的  True = ！true 
3、print  input  不是关键字 ，函数名字 不是关键字，可以作为标识符的命名  --但是 不建议使用
"""
print("全程班78期的班花是木糖醇！") #
# print("全程班77期的班草是冬瓜君！")
# print("全程班78期的班草是彭于晏！")
# print() - Python内置函数 = Python给你封装好的可以实现特定功能的东西 === 打印内容到控制台

'''
常用数据类型：整型（int），浮点型（float），字符串（str），布尔值（True =1，False=0）-bool, 列表，元组，字典，集合
整型：整数
浮点型：小数
布尔值：True =1，False=0
确认数据类型的内置函数：
1、type():直接输出数据的类型  --P1
2、isinstance() ：判断  结果是bool型--True False  --P2

字符串： 成对的引号扩起来的内容  ''  "" """ """
1、引号的嵌套使用
2、"""" 三引号 保持格式的作用 -- 所见即所得

变量：存储任何数据的容器  === 保险柜：金子，首饰，钱 ，纸，砖头，零食，衣服
变量名：  标识符命名规则 1-5点
6、变量一定要先声明，才能使用
'''
# print(type(3.1415926))
# print(isinstance(12,bool))
# print("全程班78期的班花是----"
#       "'彬彬'！")
# print('''----圆圆基本信息-----
# name：圆圆
#      gender：female
#             hobby：柠檬
# ''')
# lemon = "shdshaf"  # 把柠檬 赋值给我lemon这个变量  ==对这个 变量进行声明 ==初始化
# print(lemon)  # 打印这个变量里面存的数据

'''
需求：要在字符串里面传入变量，不想截断字符串，占位置  === 格式化是输出 
1、.format() --- P1
占位符：{}  --传变量的地方 占位置
1、可以为空=== 安装默认位置顺序进行传参 
2、指定位置进行传参  -- {}-索引
注意： 不能混用！！ 几个占位符  传几个变量
2、占位符：%s -字符串==万能  %d-数字 %f -小数  --P2 扩展
传入变量--%（）
'''
# name = "fafa"
# gender = "female"
# hobby = "柠檬"
# print('''----{}基本信息-----
# name：{}
# gender：{}
# hobby：{}
# '''.format(name,name,gender,hobby))
name = "fafa"
gender = "female"
hobby = "柠檬"
age = "18"
print('''----%s基本信息-----
name：%s
gender：%s
hobby：%s
age:%s
'''%(name,name,gender,hobby,age))





