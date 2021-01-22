#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021/1/22 13:47 
# @Author : Lemon_Tricy
# @QQ: 2378807189
# Copyright：湖南省零檬信息技术有限公司
from commen import method
from test_data import test_data
from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(10)

url = test_data.data.get("url")
username = test_data.data["username"]
password = test_data.data["password"]
key = test_data.data["search_keys"]
print(url,username,password,key)

result = method.execute_fun(driver,url,username,password,key)

if key  in result:
    print("搜索正确！")
else:
    print("搜索错误")