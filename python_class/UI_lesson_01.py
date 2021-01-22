#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021/1/18 20:54 
# @Author : Lemon_Tricy
# @QQ: 2378807189
# Copyright：湖南省零檬信息技术有限公司

"""
自动化类型：
接口自动化 ：--接口最多，稳定，性价比最高的  ==  回归测试
UI自动化：性价比低 ，做 维护成本高 === 冒烟测试
APP自动化

UI自动化：
人  -----  浏览器
Python代码    ---翻译（中间件）--    浏览器：驱动可以把代码的指令翻译给浏览器，浏览器可以做响应的操作
              浏览器驱动
             chromedriver（71版本）
             geckodriver
             ieserverdriver

selenium工具包：UI自动化工具 包括三个部分--第三方库   ==如何使用？? --Python Java
ide：-- 录制脚本 --少，不好用
webdriver:库 --- 提供了对网页各种操作的方法，提供了各种语言版本--Python java === 结合语言来用
grid：分布式 -- 同时对多个浏览器执行并发的

1、selenium安装好
2、驱动下载--Python对应的安装目录--- 浏览器安装对的
3、导入selenium webdriver

通讯原理：
1、chromedriver启动服务，IP+端口 监听
2、Python webdriver 跟 chromedriver建立连接，发送的http请求
3、chromedriver 收到指令之后，驱动浏览器把指令执行
4、chromedriver 要结果返回给 webdriver
后续指令重复步骤
"""
from selenium import webdriver  # 从selenium这个工具里面导入webdriver这个库
import time
driver = webdriver.Chrome()   # 初始化一个浏览器  --会话session
driver.get("http://baidu.com")   # 打开浏览器对应的网址
# 浏览器最大化
driver.maximize_window()
# 返回上一个页面,前进一个页面,刷新
driver.get("https://taobao.com")
time.sleep(2)
driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)
driver.refresh()
driver.close()

# 关掉浏览器：
# close() :关闭窗口，不会退出浏览器； quit() --- 退出当前会话，关闭浏览器，清楚缓存

