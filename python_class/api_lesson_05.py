#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021/1/15 19:36
# @Author : Lemon_Tricy
# @QQ: 2378807189
# Copyright：湖南省零檬信息技术有限公司
'''
第三次作业：
1：a=[1,2,'6','summer'] 请用成员运算符判断 i是否在这个列表里面 -- if
2：dict_1={"class_id":45,'num':20} 请判断班级上课人数是否大于5
注：num表示课堂人数。如果大于5，输出人数。
3、list1 = ['肥兔', '鹿鹿', 'Freestyle', '等', '地球', '阑珊', '柠檬']
列表当中的每一个值包含：姓名、性别、年龄、城市。以字典的形式表达。并且把字典都存在新的 list中，最后打印最终的列表。
方法1： 手动扩充--字典--存放在列表里面；{} --简单
方法2： 自动--dict（）--不强制-- for循环 ，list.append() --- 难度
第四次作业：
1. 把字符串转成列表
2. 完成任意整数序列的相加 - 生成一个整数序列，里面全是数字。求里面所有数字的和
3. 定义函数：判断一个对象（列表，字典，字符串）的长度是否大于5，如果大于5，输出True；否则输出False。--if 判断嵌套
'''
# def object(subject):
#     if type(subject) == list or type(subject) == dict or type(subject) == str:
#         length = len(subject)
#         if length >= 5:
#             print("Ture")
#         else:
#             print("False")
#     else:
#         print("数据类型不能计算长度！")
# object([1,2,3,4])
# object(12)
# 方式一：
# num1 = int(input("please input a num :"))
# sum1 = 0
# for i in range(num1):
#     sum1 += i
# print(sum1)
# def add_fun(num):
#     sum1 = 0
#     for i in range(num):
#         sum1 += i
#     return sum1
# result = add_fun(100)
# print("这个整数序列相加的和是：{}".format(result))

# str1 = "hello python lemon"
# list1 = list(str1)
# print(list1)
# 扩展：["hello","python","lemon"] split （str,num）: 将一个字符串以一个符号截断，返回列表--num -截取次数，默认-1==最后
# list2 = str1.split(" ",1)
# print(list2)
# a=[1,2,'6','summer']
# if "i" in a:
#     print("i是这个列表的成员！")
# else:
#     print("i不是列表的成员")
# dict_1={"class_id":45,'num':20}
# num = dict_1.get("num")  # 字典的取值
# if num > 5:
#     print("这个班级的人数是：{}".format(num))
# else:
#     print("班级人数不5人！")
# list1 = ['肥兔', '鹿鹿', 'Freestyle', '等', '地球', '阑珊', '柠檬']
# dict1 = {"name":"肥兔","gender":"male","age":18,"city":"深圳"}
# dict2 = {"name":"鹿鹿","gender":"male","age":18,"city":"深圳"}
# dict3 = {"name":"Freestyle","gender":"male","age":18,"city":"深圳"}
# dict4 = {"name":"等","gender":"male","age":18,"city":"深圳"}
# dict5 = {"name":"地球","gender":"male","age":18,"city":"深圳"}
# dict6 = {"name":"阑珊","gender":"male","age":18,"city":"深圳"}
# dict7 = {"name":"柠檬","gender":"male","age":18,"city":"深圳"}
# list2 = [dict1,dict2,dict3,dict4,dict5,dict6,dict7]
# print(list2)
# list1 = ['肥兔', '鹿鹿', 'Freestyle', '等', '地球', '阑珊', '柠檬']
# list3 = ['male', 'male', 'male', 'male', 'male', 'female', 'female']
# list4 = [18,19,20,21,22,23,24]
# list5 = ["北京","深圳","成都","重庆","北京","beijing","shenzhen"]
# list2 = []
# for i in range(len(list1)):
#     dict1 = dict(name=list1[i],gender=list3[i],age=list4[i],city=list5[i])
#     list2.append(dict1)
# print(list2)
# for item in list1:
#     dict1 = dict(name=item,gender="female",age=18,city="北京")
#     list2.append(dict1)
# print(list2)

"""
接口测试：
第三方库：别人写好的封装，拿来直接用  --- requests == Python里实现接口测试  jsonpath
1、安装 ： 
2、导入 ： import
requests方法的参数传入，除了url之外，其他的都必须用 字典格式传入

pprint -- 格式美化
"""
import requests,pprint
import jsonpath
# 注册接口
# url_api = "http://8.129.91.152:8766/futureloan/member/register"
# api_data = {
#   "mobile_phone": "15815541706",
#   "pwd": "12345678",
#   "type":"1",
#   "reg_name":"mengmeng"
# }
# head = {"X-Lemonban-Media-Type":"lemonban.v2"}
# response = requests.post(url=url_api,json=api_data,headers=head)
# print(response.json())
# 登录接口
# url_api_login = "http://8.129.91.152:8766/futureloan/member/login"
# api_data_login = {
#   "mobile_phone": "15815541706",
#   "pwd": "12345678"}
# head_login = {"X-Lemonban-Media-Type":"lemonban.v2"}
# response = requests.post(url=url_api_login,json=api_data_login,headers=head_login)
# pprint.pprint(response.json())
# res = response.json()
'''
{
'code': 0,
'copyright': 'Copyright 柠檬班 © 2017-2020 湖南省零檬信息技术有限公司 All Rights Reserved',
'data': {
          'id': 10195843,
          'leave_amount': 0.0,
          'mobile_phone': '15815541706',
          'reg_name': 'mengmeng',
          'reg_time': '2021-01-15 21:09:22.0',
          'token_info': {'expires_in': '2021-01-15 21:29:07',
                         'token': 'eyJhbGciOiJIUzUxMiJ9.eyJtZW1iZXJfaWQiOjEwMTk1ODQzLCJleHAiOjE2MTA3MTczNDd9.RR0Wp3-ug2GhwmJzG20rQEULK25fGMb66yCmTU69ju_dyZsFwTbX_ETItAZ3Dcls_2yPo50wtuEzWVq4BOzhGA',
                         'token_type': 'Bearer'},
          'type': 1},
 'msg': 'OK'
 }
'''
# 充值接口
# 字典取值 -- 接口关联
# member_id = res["data"]["id"]   # 取id
# token = res["data"]["token_info"]["token"] # 取token
# jsonpath : 安装第三方库，导入--结果放在列表里
# member_id = jsonpath.jsonpath(res,"$..id")[0]
# token = jsonpath.jsonpath(res,"$..token")[0]
# print(member_id,token)
# url_api_recharge = "http://8.129.91.152:8766/futureloan/member/recharge"
# api_data_recharge = {"member_id":member_id, "amount": 6300}
# head_rec = {"X-Lemonban-Media-Type":"lemonban.v2","Authorization":"Bearer"+" "+token}
# response = requests.post(url=url_api_recharge,json=api_data_recharge,headers=head_rec)
# pprint.pprint(response.json())

# 访问百度请求-- 扩展内容
# 1、乱码  --手动 指定解码
# 2、不是正确的页面  --爬虫 -- 反爬机制，检测到你的请求不是浏览器（）发过来，不会正确响应
# User-Agent：Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0
# https://www.baidu.com/s?wd=柠檬班

url_baidu = "https://www.baidu.com/s"
head = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0"}
param = {"wd":"柠檬班"}
response = requests.get(url=url_baidu,headers=head,params=param)
# print(response.text) # 自动解码页面--不能解码成功-再用另外换一种方法  --优先--80%
print(response.content.decode("utf8"))  # 手动指定解码方式

