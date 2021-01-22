#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021/1/17 16:07 
# @Author : Lemon_Tricy
# @QQ: 2378807189
# Copyright：湖南省零檬信息技术有限公司
"""
代码做接口自动化测试，基本流程：
1、接口文档--接口测试用例--excel里 --ready
2、自动化excel表格读取测试用例数据--得到数据 -- ready
3、执行测试-- requests去执行--执行结果  --ready
4、执行结果 vs 预期结果 对比   ---是否通过？--最终结果 =pass  failed
5、最终结果写入excel表格 ---ready--pass  failed
{'case_id': 1,
'url': 'http://api.lemonban.com/futureloan/member/register',
'data': '{"mobile_phone":"13552440101","pwd":"12345678","type":1,"reg_name":"34254sdfs"}',
'expected_result': '{"code": 0, "msg": "OK"}'}

注意： excel表格读取的数字--文本--字符串
eval(): 从字符串里面获取到Python表达式 获取
"""
from python_class import api_lesson_06   # 导入
def execute_fun(filename,sheetname):
    cases = api_lesson_06.read_data(filename,sheetname)   # 调用读取数据的函数
    for case in cases:
        case_id = case.get("case_id")
        url = case.get("url")   # 取url地址
        data = case["data"]  # 取测试参数
        data = eval(data)   # 从字符串里面获取到Python表达式  --字典
        expected_result = case.get("expected_result")
        expected_result = eval(expected_result) # 从字符串里面获取到Python表达式  --字典
        expected_msg = expected_result.get("msg")
        real_result = api_lesson_06.api_func(url_api=url,data_api=data)   # 调用接口发送的参数
        real_msg = real_result.get("msg")
        print("真实执行结果：{}".format(real_msg))
        print("预期执行结果：{}".format(expected_msg))
        if real_msg == expected_msg:
            final_result = "Passed"   # 标识最终的结果
            print("第{}条测试用例执行通过！".format(case_id))
        else:
            final_result = "Failed"
            print("第{}条测试用例执行不通过！".format(case_id))
        print("*" * 20)
        api_lesson_06.write_result(filename,sheetname,final_result,case_id+1,8)  # 调用写入结果函数的

# execute_fun("test_case_api.xlsx","login")

"""
在已有的框架下实现的自动化的脚本
完整自动化框架：
1、基础代码
2、测试数据
3、报告、日志
"""






