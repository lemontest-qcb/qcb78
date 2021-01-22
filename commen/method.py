#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021/1/22 13:45 
# @Author : Lemon_Tricy
# @QQ: 2378807189
# Copyright：湖南省零檬信息技术有限公司

# 登录函数
import time
def open_web(driver,url):
    driver.get(url)
    driver.maximize_window()

def login_fun(driver,username,passwd):
    driver.find_element_by_id("username").send_keys(username)  # 输入用户名
    driver.find_element_by_id("password").send_keys(passwd)  # 输入密码
    driver.find_element_by_xpath("//input[@id='rememberUserCode']/following-sibling::ins").click()
    driver.find_element_by_id("btnSubmit").click()

def execute_fun(driver,url,username,password,search_key):
    open_web(driver,url)
    login_fun(driver,username,password)
    driver.find_element_by_xpath("//span[text()='零售出库']").click()
    id_par = driver.find_element_by_xpath('//div[text()="零售出库"]/..').get_attribute("id")
    id_frame = id_par + "-frame"
    driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@id='{}']".format(id_frame)))
    driver.find_element_by_id('searchNumber').send_keys(search_key)
    driver.find_element_by_id("searchBtn").click()
    time.sleep(2)
    result = driver.find_element_by_xpath("//tr[@id='datagrid-row-r1-2-0']//td[@field='number']/div").text
    return result

if __name__ == '__main__':

    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    url = "http://erp.lemfix.com"

    re = execute_fun(driver,url,"test123","123456","712")
    print(re)