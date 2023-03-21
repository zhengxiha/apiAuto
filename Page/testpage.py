#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2023/3/13 16:07
# @Author : xiha
# @File : testpage.py
# @Editor : PyCharm

from selenium.webdriver.common.by import By


# Function：打开百度网主页，在搜索栏输入“helloworld”

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# driver = webdriver.Chrome()  # 打开Chrome浏览器
driver = webdriver.Edge()
driver.get("http://www.baidu.com")  # 输入百度网址

print("============验证浏览器的基本控制==========")

def search():
    print("1、搜索helloworld.并回车......")
    time.sleep(2)
    driver.find_element(By.ID,"kw").send_keys("helloworld")  # 输入“helloworld”
    time.sleep(2)
    driver.find_element(By.ID,"kw").send_keys(Keys.ENTER)  # 回车进行搜索
    time.sleep(2)
    driver.maximize_window()  # 最大化当前窗口


def windows_size():
    print("2、浏览器窗口大小缩小为640*480......")
    time.sleep(2)
    driver.set_window_size(640, 480)  # 控制浏览器显示尺寸为640*480
    time.sleep(0.5)
    driver.maximize_window()  # 最大化当前窗口
    time.sleep(2)

def back_refresh():
    print("3、先进行浏览器后退，再次输入csdn进行搜索")
    driver.back()
    driver.find_element(By.ID,"kw").send_keys("csdn")  # 输入csdn
    time.sleep(1)
    driver.refresh() # 刷新

def serach_clear():
    print("4、清空输入的内容......")
    driver.find_element(By.ID,"kw").send_keys("csdn")  # 输入csdn
    time.sleep(2)
    driver.find_element(By.ID,"kw").clear()
    time.sleep(0.5)

def csdn():
    print("5、进入csdn官网")
    driver.find_element(By.ID,"kw").send_keys("csdn")  # 输入csdn
    time.sleep(2)
    driver.find_element(By.ID,"kw").send_keys(Keys.ENTER)  # 回车进行搜索
    time.sleep(2)
    driver.find_element(By.XPATH,"//*[@id='1']/div/div[1]/h3/a[1]").click()
    time.sleep(2)
    windows = driver.window_handles
    driver.switch_to.window(windows[-1])
    now_url = driver.current_url
    m_get_url = "https://www.csdn.net/"
    if now_url == m_get_url:
        print("经过判断，已经进入csdn官网！！")
    else:
        print("未进入到csdn官网，请检查代码！")

search()
windows_size()
back_refresh()
serach_clear()
csdn()

driver.quit()  # 关闭浏览器