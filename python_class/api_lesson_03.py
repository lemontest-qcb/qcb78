#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021/1/11 19:26
# @Author : Lemon_Tricy
# @QQ: 2378807189
# Copyright：湖南省零檬信息技术有限公司
'''
第二次作业：
1、在pycharm的控制台里输入以下内容，并且以如下格式输出到控制台
2、现在有字符串：str1 = 'python hello aaa 123123aabb'
1）请取出并打印字符串中的'python'。
2）请分别判断 'o a' 'he' 'ab' 是否是该字符串中的成员？
3）替换python为 “lemon”.
4) 找到aaa的起始位置
'''
# name = input("请输入你的名字：")
# age = input("请输入你的年龄：")
# gender = input("请输入你的性别：")
# print('''********************
# 姓名：{}
# 年龄：{}
# 性别：{}
# ********************'''.format(name,age,gender))
# str1 = 'python hello aaa 123123aabb'
# print(str1[0:6:1])
# print("o a" in str1)
# print("he" in str1)
# print(str1.replace("python","lemon"))
# print(str1.find("aaa"))
# print(str1.index("aaa"))
'''
数据类型：int  float bool  str list  元组 dict set
列表：list  [] 
1、列表可以存放任意数据类型 ,包括列表，元素和元素之间用英文逗号隔开
2、列表统计元素个数：len()
3、取值：每个元素都有自己的位置---索引，从0开始  最后一个元素 - -1
   取多个值：切片  
扩展：列表的嵌套 如何取值？--list1[4][2]
3、列表的元素可以被改变的：增加、删除、修改
4、列表的元素是可以重复的  重复的次数--count()
# '''
# list1 = [20,3.14,True,"Freestyle",[1,2,4,5]]  # 定义了一个列表 --空列表
# print(list1)
# print(list1[3])
# print(list1[4][2])
# # 增加
# list1.append("等")  # 追加元素到末尾  --p1
# print(list1)
# list1.insert(3,"鹿鹿")  # 指定位置进行元素的增加 ---p1
# print(list1)
# list1.extend(["地球","阑珊","柠檬"])  # 合并，可以同时添加多个元素 --扩展
# print(list1)
# # 删除
# list1.pop(5)  # 1、默认删除最后一个元素  2、可以指定元素的索引进行删除
# print(list1)
# list1.remove(20)  # 指定元素本身进行删除
# print(list1)
# # list1.clear()  # 清除 清空列表
# # 修改 -- 进行重新赋值
# list1[0] = "肥兔"
# print(list1)
# list1[1] = "肥兔"
# list1.append("肥兔")
# print(list1)
# print(list1.count("肥兔"))
'''
元组：tuple ()
1、元组可以存放任意数据类型 ，元素和元素之间用英文逗号隔开
2、元组统计元素个数：len()
3、取值：每个元素都有自己的位置---索引，从0开始  最后一个元素 - -1
   取多个值：切片  
3、元组的元素不可以被改变的
4、列表的元素是可以重复的  重复的次数--count()

扩展：想要改变元组的元素？ -- 列表--list()  元组--tuple()
'''
# tuple1 = ('肥兔', '肥兔', '鹿鹿', 'Freestyle', '等', '地球', '阑珊', '柠檬')
# print(tuple1)
# # tuple1[0] = "简单"
# # print(tuple1)
# list2 = list(tuple1)
# print(list2)
# list2[0] = "简单"
# print(list2)
# tuple2 = tuple(list2)
# print(tuple2)
'''
字典：dict {}
1、元素是键值对的格式：key：value  --一个键值对是一个元素，多个元素之间用逗号隔开
2、字典一般的使用场景：描述一个物件的属性 == 人的属性：名字，年龄，性别  == key：value
3、取值：通过key 来取value值== 2个都要掌握
注意：字典在3.6版本之前没有顺序的，没有索引的 
4、key的要求：1）是不可变的（不可以是列表，字典），2）key 不可以重复的；--唯一性
  value的要求：没有任何要求 -- 可以被改变- 增加 删除 修改
5、统计元素个数 --len()
'''
dict1 = {"name":"hcalb","age":'18',"gender":"Male"}
# print(dict1["age"])
# print(dict1.get("age"))
# print(dict1.keys())  # 了解
# print(dict1.values())
# print(dict1.items())
# 增加 / 修改--  加一个键值对
dict1["hobby"] = "女"   # 如果key不存在的，新增加一个键值对--元素
print(dict1)
dict1["gender"] = "Female"    # 如果key存在的，更新一个键值对的value
dict1["hobby"] = "男"
print(dict1)
# 增加多个？ -- update 字典  ==字典的合并操作
dict1.update({"city":"深圳","weight":"130","hight":"180"})
# 删除 --指定key进行删除
# dict1.pop("hobby")
print(dict1)
# print(len(dict1))
'''
集合：set  {}，元素单个  ==工作中非常少  --扩展
1、集合的元素不重复的  == 使用场景就是给列表去重
2、无序的
'''
# list3 = [22,11,11,33,44,55,55]
# # 获取列表里出现过的元素  -- 去重
# set1 = set(list3)  # 转化为集合
# print(set1)
# list4 = list(set1)
# print(list4)
# print(set(list3))

'''
控制流：if判断  for循环  == 分支
if判断语法：
if 条件： ---- 判断这个条件成立的时候话，进入下面的执行语句-分支  == 冒号，四个空格的缩进
    子代码（执行语句）
elif 条件：判断这个条件成立的时候话，进入下面的执行语句-分支
    子代码（执行语句）
elif 条件：  ==注意： elif可以没有 可以有多个
    子代码（执行语句）
    .
    .
    .
else: --- 没有条件的
    子代码（执行语句）
'''
# money = int(input("请输入你的余额："))  # input得到的是— 字符串
# if money >= 200:
#     print("做生意！")
# elif money >= 100:
#     print("买房！")
# elif money >= 50:
#     print("买车！")
# elif money >= 20:
#     print("买点零食，吃吃")
# else:
#     print("打工人好好工作，学习！")

'''
for循环：重复执行某一块代码
使用场景：用来遍历某些数据对象的元素的。 -- 字符串，列表，元组，字典？
缩进里面是for循环的循环体 
问题1: 循环次数由谁决定的？--- 元素的个数
问题2：如何控制循环？ -- if判断， break  continue 

for循环结合一起使用一个内置函数：range（start，stop，step）-- 生成一个整数序列
start：从谁开始生成 ，默认值-- 0开始
stop：到谁结束 --不能省略   == 取头不取尾
step：步长  默认值-- 1 
'''
# count = 0
# str1 = "我爱柠檬班！"
# for i in str1:
#     print(i)
#     print("*" * 20)
#     count += 1
# print(len(str1))
# print(count)
# list1 = ['肥兔', '鹿鹿', 'Freestyle', '等', '地球', '阑珊', '柠檬']
# for name in list1:
#     if name == "等":
#         # break   # 中断 --跳出整个循环
#         continue  # 继续--跳出本次循环
#     print(name)
# for num in range(0,11,2):
#     print(num)

# 总结一下，目前学到了哪些内置函数？ print（），input（）
dict2 = {"name":"Tricy","age":18}
dict3 = dict(name="Tricy",age=18,city="changsha")
print(dict2)
print(dict3)